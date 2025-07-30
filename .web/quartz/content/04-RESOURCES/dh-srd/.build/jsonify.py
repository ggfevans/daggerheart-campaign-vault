import csv
import json
import os
import re
from collections import OrderedDict, defaultdict
from titlecase import titlecase
import inflect

# Set up the inflect engine for pluralization
p = inflect.engine()


def normalize_header(header):
    return header.strip().lower().replace(" ", "_")


def pluralize(word):
    return p.plural(word)


def group_digit_fields(fieldnames):
    """
    Finds headers with a digit (e.g., 'Feat 1 Name') and groups them.
    Returns: (regular_fields, grouped_fields)
    grouped_fields: dict of {prefix: [list of (index, subfield, original name, normalized)]}
    """
    regular_fields = []
    grouped_fields = defaultdict(list)
    # Pattern: prefix, digit, rest
    pattern = re.compile(r"^(.*?)[ _-](\d+)[ _-](.*)$", re.I)
    for orig in fieldnames:
        m = pattern.match(orig)
        if m:
            prefix, index, subfield = m.groups()
            group_key = normalize_header(prefix)
            subfield_key = normalize_header(subfield)
            grouped_fields[group_key].append(
                (int(index), subfield_key, orig, normalize_header(orig))
            )
        else:
            regular_fields.append((orig, normalize_header(orig)))
    # Sort the grouped fields by their index
    for key in grouped_fields:
        grouped_fields[key].sort(key=lambda tup: tup[0])
    return regular_fields, grouped_fields


def csv_to_json(csv_path, json_path):
    """Converts a CSV file to a JSON file, grouping digit fields into lists."""
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(csv_path, newline="", encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        if not reader.fieldnames:
            return  # skip empty CSVs

        # Analyze headers
        regular_fields, grouped_fields = group_digit_fields(reader.fieldnames)
        data = []
        for row in reader:
            ordered_row = OrderedDict()
            # Regular fields
            for orig, norm in regular_fields:
                value = row[orig]
                if value is None:
                    continue
                value = value.strip()
                if value == "":
                    continue
                if norm == "name":
                    value = titlecase(value)
                ordered_row[norm] = value
            # Grouped fields (feats, features, etc.)
            for group, fields in grouped_fields.items():
                group_dicts = defaultdict(dict)
                # Each field: (index, subfield, orig, norm)
                for index, subfield, orig, norm in fields:
                    value = row[orig]
                    if value is None:
                        continue
                    value = value.strip()
                    if value == "":
                        continue
                    group_dicts[index][subfield] = value
                # Convert to list, skipping empty dicts
                group_list = [v for k, v in sorted(group_dicts.items()) if v]
                if group_list:
                    ordered_row[pluralize(group)] = group_list
            if ordered_row:  # only append non-empty rows
                data.append(ordered_row)
    with open(json_path, "w", encoding="utf-8-sig") as jsonfile:
        json.dump(data, jsonfile, indent=2, ensure_ascii=False)


def main():
    csv_dir = "csv"
    json_dir = "json"
    os.makedirs(json_dir, exist_ok=True)
    for filename in os.listdir(csv_dir):
        if filename.lower().endswith(".csv"):
            csv_path = os.path.join(csv_dir, filename)
            json_filename = os.path.splitext(filename)[0] + ".json"
            json_path = os.path.join(json_dir, json_filename)
            print(f"Converting {csv_path} → {json_path}")
            csv_to_json(csv_path, json_path)


if __name__ == "__main__":
    main()
