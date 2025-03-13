# SIAPE-CLI

SIAPE-cli is a Python package designed to facilitate interaction with the [SIAPE website](https://siape.enea.it/). This tool allows users to download and filter data related to energy efficiency certifications of buildings in Italy.

---

## 🌟 Features

- Filter building-related data using geolocation, qualitative features, climatic zones, and other criteria.
- Enforce admissible combinations for filter options.
- Download results as a CSV file with customizable filenames.

---

## 🚀 Installation

### From PyPI

```bash
pip install siape-cli
```

After installation, the package provides a `download` command to filter and export building-related data.

---

### 🛠️ Command-Line Interface (CLI)

You can invoke the CLI using the `siape-cli` command:

```bash
siape-cli download [OPTIONS]
```

### Options

| Option                   | Description                                           | Allowed Values       |
|--------------------------|-------------------------------------------------------|----------------------|
| `-g`, `--geolocation`    | Filter by geolocation (region or province).           | `reg`, `prov`        |
| `-q`, `--qualitative_features` | Filter by qualitative features (years, surface, or both). | `y`, `s`, `ys`        |
| `-r`, `--resid`          | Filter by building type (Residential/Non-Residential).| `res`, `non-res`     |
| `-z`, `--zon_cli_filter` | Filter by climatic zones.                             | -                    |
| `-d`, `--dp412`          | Filter by law DP412/93.                               | -                    |
| `-n`, `--nzeb`           | Filter by NZEB buildings only.                        | -                    |
| `-o`, `--output`         | Specify output file name (default: `<timestamp>.csv`).| -                    |

---

## 🖋️ Examples

1. **Download data for residential buildings in regions**:
   ```bash
   siape-cli download -g reg -r res
   ```

2. **Filter by climatic zone and qualitative features**:
   ```bash
   siape-cli download -z -q ys
   ```

3. **Download NZEB buildings data and save as `nzeb_data.csv`**:
   ```bash
   siape-cli download -n -o nzeb_data.csv
   ```

4. **Filter using `dp412` law in provinces**:
   ```bash
   siape-cli download -d -g prov
   ```

---

## 🚫 Rules and Restrictions

To maintain data integrity, the tool enforces the following admissible combinations:

```
reg
prov
y
s
ys
zc
dp412
reg, zc
reg, prov
reg, prov, zc
y, zc
s, zc
dp412, reg
dp412, prov
dp412, zc
dp412, y
dp412, s
dp412, ys
```

Using an invalid combination will produce an error:
```plaintext
NotAdmissibleCombination: Combination of arguments <args_set> is not admissible.
```

---
 
## 🧑‍💻 Contribution

Contributions are welcome! So far only the main filtering arguments have been implemented, and more features can be added to enhance the tool. Follow these steps to get started:

1. Open an issue to discuss the feature/fix.
2. Fork the repository.
3. Create a new branch for your feature/fix.
4. Commit your changes and push the branch.
5. Open a pull request for review.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).