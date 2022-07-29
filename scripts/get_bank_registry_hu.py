#!/usr/bin/env python
import json
import pandas


URL = "https://www.mnb.hu/letoltes/sht.xlsx"


def process():
    registry = []
    sheet = pandas.read_excel(URL, sheet_name=0, dtype="str")

    for row in sheet.itertuples(index=False):
        bank_code, bic, name = row[:3]

        print(row)
        registry.append(
            {
                "country_code": "HU",
                "primary": True,
                "bic": str(bic).upper().replace(" ", ""),
                "bank_code": str(bank_code),
                "name": name,
                "short_name": name,
            }
        )

    print(f"Fetched {len(registry)} bank records")
    return registry


if __name__ == "__main__":
    with open("schwifty/bank_registry/generated_hu.json", "w") as fp:
        json.dump(list(process()), fp, indent=2)
