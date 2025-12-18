import pandas as pd

EXCEL_PATH = "Literature_Survey.xlsx"

print("\n=== EXCEL INTEGRATION TEST ===\n")

# =========================
# 1) CHECK SHEET NAMES
# =========================
try:
    xls = pd.ExcelFile(EXCEL_PATH)
    print("Sheets found:")
    for sheet in xls.sheet_names:
        print(f"- {sheet}")
except Exception as e:
    print("❌ ERROR: Excel file could not be loaded")
    print(e)
    exit()

# =========================
# 2) TEST MATERIAL PROPERTIES SHEET
# =========================
print("\n--- Testing Material_Properties sheet ---")

try:
    material_df = pd.read_excel(EXCEL_PATH, sheet_name="Material_Properties")
    print("✅ Material_Properties loaded")

    print("\nColumns:")
    for col in material_df.columns:
        print(f"- {repr(col)}")

    print("\nSample rows:")
    print(material_df.head(5))

    print("\nTotal rows:", len(material_df))

except Exception as e:
    print("❌ ERROR loading Material_Properties")
    print(e)

# =========================
# 3) TEST SPECIAL CLINICAL CONDITIONS SHEET
# =========================
print("\n--- Testing Special_Clinical_Conditions sheet ---")

try:
    special_df = pd.read_excel(EXCEL_PATH, sheet_name="Special_Clinical_Conditions")
    print("✅ Special_Clinical_Conditions loaded")

    print("\nColumns:")
    for col in special_df.columns:
        print(f"- {repr(col)}")

    print("\nSample rows:")
    print(special_df.head(5))

    print("\nUnique Conditions:")
    if "Condition" in special_df.columns:
        print(special_df["Condition"].dropna().unique())
    else:
        print("⚠️ Column 'Condition' NOT FOUND")

except Exception as e:
    print("❌ ERROR loading Special_Clinical_Conditions")
    print(e)

# =========================
# 4) PARAMETER MATCHING TEST
# =========================
print("\n--- Testing parameter matching ---")

if "Parametre" in material_df.columns:
    excel_params = material_df["Parametre"].dropna().unique().tolist()
    print(f"Total unique parameters in Excel: {len(excel_params)}")

    print("\nFirst 10 parameters:")
    for p in excel_params[:10]:
        print(f"- {repr(p)}")
else:
    print("❌ Column 'Parametre' NOT FOUND")

print("\n=== TEST FINISHED ===\n")
