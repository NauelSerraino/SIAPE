from itertools import product

from siape_tool.utils.constants import (
    SURFACE_LIMITS, 
    YEARS_LIMITS, 
    ZONCLI, 
    CODREG, 
    COMBS_DP412_93_RESID, 
    CODREG_TO_PROV
)

"""
Here we define all the possible combinations of the API calls that we need to make.
"""

# COMBINATIONS OF API'S PARAMETERS
COMBS_YEARS_SURFACE = list(product(YEARS_LIMITS, SURFACE_LIMITS))
COMBS_YEARS_SURFACE_ZONCLI = list(product(YEARS_LIMITS, SURFACE_LIMITS, ZONCLI))
COMBS_YEARS_ZONCLI = list(product(YEARS_LIMITS, ZONCLI))
COMBS_SURFACE_ZONCLI = list(product(SURFACE_LIMITS, ZONCLI))
COMBS_REG_ZONCLI = list(product(CODREG, ZONCLI))
COMBS_REG_PROV = [
    [reg, prov] 
    for reg in CODREG_TO_PROV.keys() 
    for prov in CODREG_TO_PROV[reg]
    ]
COMSB_REG_PROV_ZONCLI = [
    [reg, prov, zoncli]
    for reg in CODREG_TO_PROV.keys()
    for prov in CODREG_TO_PROV[reg]
    for zoncli in ZONCLI
]

# LIST OF PAYLOADS - Single combinations
STANDARD_PAYLOAD = [
    {
        "group[]": "claen",
        "nofilter": "false",
    }
]

NATIONAL_ZONCLI_PAYLOAD = [
    {
        "group[]": "claen",
        "where[zoncli]": ZONCLI[i],
        "nofilter": "false",
    }
    for i in range(len(ZONCLI))
]

COMBS_REG_PAYLOAD = [
    {
        "group[]": "claen",
        "where[cod_reg]": CODREG[i],
        "nofilter": "false",
    }
    for i in range(len(CODREG))
]

COMBS_YEARS_PAYLOAD = [
    {
        "group[]": "claen",
        "nofilter": "false",
        "where[annoc][range][]": YEARS_LIMITS[i],
    }
    for i in range(len(YEARS_LIMITS))
]

COMBS_SURFACE_PAYLOAD = [
    {
        "group[]": "claen",
        "nofilter": "false",
        "where[suris][range][]": SURFACE_LIMITS[i],
    }
    for i in range(len(SURFACE_LIMITS))
]

COMBS_DP412_93 = [
    {
        "group[]": "claen",
        "where[destuso]": value,
        "where[dpr412]": key,
        "nofilter": "false",
    }
    for key, value in COMBS_DP412_93_RESID.items()
]

# LIST OF PAYLOADS - Combined combinations (Admissible combinations)
COMBS_YEARS_SURFACE_PAYLOAD = [
    {
        "group[]": "claen",
        "nofilter": "false",
        "where[annoc][range][]": COMBS_YEARS_SURFACE[i][0],
        "where[suris][range][]": COMBS_YEARS_SURFACE[i][1],
    }
    for i in range(len(COMBS_YEARS_SURFACE))
]

COMBS_REG_PROV_PAYLOAD = [
    {
        "group[]": "claen",
        "where[cod_reg]": COMBS_REG_PROV[i][0],
        "where[cod_pro]": COMBS_REG_PROV[i][1],
        "nofilter": "false",
    }
    for i in range(len(COMBS_REG_PROV))
]

COMBS_REG_ZONCLI_PAYLOAD = [
    {
        "group[]": "claen",
        "where[cod_reg]": COMBS_REG_ZONCLI[i][0],
        "where[zoncli]": COMBS_REG_ZONCLI[i][1],
        "nofilter": "false",
    }
    for i in range(len(COMBS_REG_ZONCLI))
]

COMBS_REG_PROV_ZONCLI_PAYLOAD = [
    {
        "group[]": "claen",
        "where[cod_reg]": COMSB_REG_PROV_ZONCLI[i][0],
        "where[cod_pro]": COMSB_REG_PROV_ZONCLI[i][1],
        "where[zoncli]": COMSB_REG_PROV_ZONCLI[i][2],
        "nofilter": "false",
    }
    for i in range(len(COMSB_REG_PROV_ZONCLI))
]

COMBS_YEARS_ZONCLI_PAYLOAD = [
    {
        "group[]": "claen",
        "nofilter": "false",
        "where[annoc][range][]": COMBS_YEARS_ZONCLI[i][0],
        "where[zoncli]": COMBS_YEARS_ZONCLI[i][1],
    }
    for i in range(len(COMBS_YEARS_ZONCLI))
]

COMBS_SURFACE_ZONCLI_PAYLOAD = [
    {
        "group[]": "claen",
        "nofilter": "false",
        "where[suris][range][]": COMBS_SURFACE_ZONCLI[i][0],
        "where[zoncli]": COMBS_SURFACE_ZONCLI[i][1],
    }
    for i in range(len(COMBS_SURFACE_ZONCLI))
]

COMBS_YEARS_SURFACE_ZONCLI_PAYLOAD = [
    {
        "group[]": "claen",
        "nofilter": "false",
        "where[annoc][range][]": COMBS_YEARS_SURFACE_ZONCLI[i][0],
        "where[suris][range][]": COMBS_YEARS_SURFACE_ZONCLI[i][1],
        "where[zoncli]": COMBS_YEARS_SURFACE_ZONCLI[i][2],
    }
    for i in range(len(COMBS_YEARS_SURFACE_ZONCLI))
]

COMBS_DP412_REG = [
    {
        "group[]": "claen",
        "where[destuso]": value,
        "where[dpr412]": key,
        "where[cod_reg]": reg,
        "nofilter": "false",
    }
    for key, value in COMBS_DP412_93_RESID.items()
    for reg in CODREG
]

COMBS_DP412_REG_PROV = [
    {
        "group[]": "claen",
        "where[destuso]": value,
        "where[dpr412]": key,
        "where[cod_reg]": reg,
        "where[cod_pro]": prov,
        "nofilter": "false",
    }
    for key, value in COMBS_DP412_93_RESID.items()
    for reg in CODREG_TO_PROV.keys()
    for prov in CODREG_TO_PROV[reg]
]

COMBS_DP412_ZONCLI = [
    {
        "group[]": "claen",
        "where[destuso]": value,
        "where[dpr412]": key,
        "where[zoncli]": zoncli,
        "nofilter": "false",
    }
    for key, value in COMBS_DP412_93_RESID.items()
    for zoncli in ZONCLI
]

COMBS_DP412_YEARS = [
    {
        "group[]": "claen",
        "where[destuso]": value,
        "where[dpr412]": key,
        "where[annoc][range][]": year,
        "nofilter": "false",
    }
    for key, value in COMBS_DP412_93_RESID.items()
    for year in YEARS_LIMITS
]

COMBS_DP412_SURFACE = [
    {
        "group[]": "claen",
        "where[destuso]": value,
        "where[dpr412]": key,
        "where[suris][range][]": surface,
        "nofilter": "false",
    }
    for key, value in COMBS_DP412_93_RESID.items()
    for surface in SURFACE_LIMITS
]

COMBS_DP412_YEARS_SURFACE = [
    {
        "group[]": "claen",
        "where[destuso]": value,
        "where[dpr412]": key,
        "where[annoc][range][]": year,
        "where[suris][range][]": surface,
        "nofilter": "false",
    }
    for key, value in COMBS_DP412_93_RESID.items()
    for year in YEARS_LIMITS
    for surface in SURFACE_LIMITS
]

# ADMISSIBLE COMBINATIONS
ADMISSIBLE_COMBINATIONS = [
    frozenset({"reg"}),                # Region only
    frozenset({"prov"}),               # Province only
    frozenset({"y"}),                  # Years only
    frozenset({"s"}),                  # Surface only
    frozenset({"ys"}),                 # Years and Surface
    frozenset({"zc"}),                 # Zoncli only
    frozenset({"dp412"}),              # DP412 only
    frozenset({"reg", "zc"}),          # Region and Zoncli
    frozenset({"reg", "prov"}),        # Region and Province
    frozenset({"reg", "prov", "zc"}),  # Region, Province, and Zoncli
    frozenset({"y", "zc"}),            # Years and Zoncli
    frozenset({"s", "zc"}),            # Surface and Zoncli
    frozenset({"ys", "zc"}),           # Years, Surface, and Zoncli
    frozenset({"dp412", "reg"}),       # DP412 and Region
    frozenset({"dp412", "prov"}),      # DP412 and Province
    frozenset({"dp412", "zc"}),        # DP412 and Zoncli
    frozenset({"dp412", "y"}),         # DP412 and Years
    frozenset({"dp412", "s"}),         # DP412 and Surface
    frozenset({"dp412", "ys"}),        # DP412 and Years and Surface
]

PAYLOAD_COMBS = {
    frozenset({"reg"}): COMBS_REG_PAYLOAD,
    frozenset({"prov"}): COMBS_REG_PROV_PAYLOAD,
    frozenset({"y"}): COMBS_YEARS_PAYLOAD,
    frozenset({"s"}): COMBS_SURFACE_PAYLOAD,
    frozenset({"zc"}): NATIONAL_ZONCLI_PAYLOAD,
    frozenset({"ys"}): COMBS_YEARS_SURFACE_PAYLOAD,
    frozenset({"dp412"}): COMBS_DP412_93,
    frozenset({"reg", "zc"}): COMBS_REG_ZONCLI_PAYLOAD,
    frozenset({"prov", "zc"}): COMBS_REG_PROV_ZONCLI_PAYLOAD,
    frozenset({"y", "zc"}): COMBS_YEARS_ZONCLI_PAYLOAD,
    frozenset({"s", "zc"}): COMBS_SURFACE_ZONCLI_PAYLOAD,
    frozenset({"ys", "zc"}): COMBS_YEARS_SURFACE_ZONCLI_PAYLOAD,
    frozenset({"dp412", "reg"}): COMBS_DP412_REG,
    frozenset({"dp412", "prov"}): COMBS_DP412_REG_PROV,
    frozenset({"dp412", "zc"}): COMBS_DP412_ZONCLI,
    frozenset({"dp412", "y"}): COMBS_DP412_YEARS,
    frozenset({"dp412", "s"}): COMBS_DP412_SURFACE,
    frozenset({"dp412", "ys"}): COMBS_DP412_YEARS_SURFACE,
}
