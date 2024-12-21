from itertools import product

from siape_tool.utils.constants import SURFACE_LIMITS, YEARS_LIMITS, ZONCLI, CODREG, COMBS_DP412_93_RESID, CODREG_TO_PROV

"""
Here we define all the possible combinations of the API calls that we need to make.
"""

COMBS_YEARS_SURFACE = list(product(YEARS_LIMITS, SURFACE_LIMITS))
COMBS_YEARS_SURFACE_ZONCLI = list(product(YEARS_LIMITS, SURFACE_LIMITS, ZONCLI))
COMBS_YEARS_ZONCLI = list(product(YEARS_LIMITS, ZONCLI))
COMBS_SURFACE_ZONCLI = list(product(SURFACE_LIMITS, ZONCLI))
COMBS_REG_ZONCLI = list(product(CODREG, ZONCLI))
COMBS_REG_PROV = [[reg, prov] for reg in CODREG_TO_PROV.keys() for prov in CODREG_TO_PROV[reg]]
COMSB_REG_PROV_ZONCLI = [
    [reg, prov, zoncli]
    for reg in CODREG_TO_PROV.keys()
    for prov in CODREG_TO_PROV[reg]
    for zoncli in ZONCLI
]

COMBS_YEARS_SURFACE_PAYLOAD = [
    {
        "group[]": "claen",
        "nofilter": "false",
        "where[annoc][range][]": COMBS_YEARS_SURFACE[i][0],
        "where[suris][range][]": COMBS_YEARS_SURFACE[i][1],
    }
    for i in range(len(COMBS_YEARS_SURFACE))
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

COMBS_REG_PAYLOAD = [
    {
        "group[]": "claen",
        "where[cod_reg]": CODREG[i],
        "nofilter": "false",
    }
    for i in range(len(CODREG))
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

COMBS_REG_PROV_PAYLOAD = [
    {
        "group[]": "claen",
        "where[cod_reg]": COMBS_REG_PROV[i][0],
        "where[cod_pro]": COMBS_REG_PROV[i][1],
        "nofilter": "false",
    }
    for i in range(len(COMBS_REG_PROV))
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

COMBS_DP412_93_RESID_NATIONAL_PAYLOAD = [
    {
        "group[]": "claen",
        "where[destuso]": value,
        "where[dpr412]": key,
        "where[zoncli]": ZONCLI[j],
        "where[annoc][range][]": YEARS_LIMITS[z],
        "nofilter": "false",
    }
    for key, value in COMBS_DP412_93_RESID.items()
    for j in range(len(ZONCLI))
    for z in range(len(YEARS_LIMITS))
]