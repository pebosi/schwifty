#!/usr/bin/env python
import json
import pandas


URL = "https://www.finanssiala.fi/wp-content/uploads/2021/03/Finnish_monetary_institution_codes_and_BICs_in_excel_format.xlsx"


def process():
    sheet = pandas.read_excel(URL, skiprows=2, sheet_name=0, dtype=str)

    return [
        {
            "country_code": "FI",
            "primary": True,
            "bic": str(bic).upper().strip(),
            "bank_code": bank_code,
            "name": name,
            "short_name": name,
        }
        for bank_code, bic, name in list(sheet.itertuples(index=False))[2:]
        if bank_code != ""
    ]


if __name__ == "__main__":
    with open("schwifty/bank_registry/generated_fi.json", "w") as fp:
        json.dump(process(), fp, indent=2)
