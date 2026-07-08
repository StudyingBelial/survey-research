# Data Interpretation and Preprocessing Notes

This document details the data cleaning, preprocessing, and mapping rules applied to the survey research dataset.

---

## 1. Removed Values

### NaN Values
Row entries containing `NaN` values in the following columns were removed:

| Column | Removed NaN Count |
| :--- | :--- |
| `Which industry are you working for?` | 1 |
| `What is your occupation?` | 1 |
| `Having national laws that enforce ethical and socially responsible AI use` | 1 |
| `Voluntary certifications from trusted organizations ensuring ethical standards` | 1 |
| `Independent experts monitoring AI use and informing the public` | 2 |
| `Companies following a self-regulated code of ethics for AI development` | 2 |
| `Clear and transparent explanations about what the AI does and how it uses data` | 2 |
| `Inclusion of diverse teams and stakeholder consultation throughout AI development` | 3 |

### Explicit Index Removal
- **Index 11**: Removed explicitly because `residence_country` was set to `"Bides"` (abroad).

---

## 2. Text Preprocessing

All text columns are cleaned using the following operations:
1. **ASCII Filtering**: Retaining only ASCII characters.
2. **Case Normalization**: Converting all text to lowercase.
3. **Whitespace Truncation**: Stripping leading and trailing whitespaces.

All subsequent mapping operations assume that this preprocessing has been applied.

---

## 3. Feature Mappings

### Occupation Mapping
Occupations are grouped into the following broad categories:
- `student`
- `unemployed`
- `teacher`
- `engineering/tech`
- `management/business`
- `medical`
- `other`

*Note on sparse values:* Statistically insignificant occupation responses (appearing only once or twice) were either grouped into `other` or combined using a slash (`/`).

### Ethnicity Mapping
Ethnicity responses are mapped as follows:

| Original Response | Mapped Category |
| :--- | :--- |
| `asian` | `asian` |
| `african` | `african/non-asian` |
| `american indian` | `asian` |
| `latino` | `african/non-asian` |
| `nepali` | `asian` |
| `black african/african american` | `african/non-asian` |
| `indian` | `asian` |
| `bramin` | `asian` |

*Note on Latino grouping:* The category `latino` is grouped with `african/non-asian`. While African respondents represented a statistically significant portion of the sample, classifying Latino respondents directly as "African" would be a gross oversimplification. They are instead combined into this broader non-Asian category.

### Language Mapping
Languages are grouped into the following broad categories:
- `english`
- `nepali_dominant`
- `south_asian_other`
- `global_other`
- `african_other`

*Key Distinctions:*
- **`nepali_dominant` vs. `south_asian_other`**: The `nepali_dominant` category is used specifically for languages that originate in Nepal or have a sizable Nepalese speaker population. Other languages from the South Asian region are mapped to `south_asian_other`.
- **`african_other`**: Individual African languages or countries are collected into a single category (`african_other`) because individual counts were too sparse to be statistically meaningful. This category groups languages that have their origin or a majority of speakers on the African continent.

### Region Mapping
Countries and regions are mapped as follows:

| Original Country/Region | Mapped Category |
| :--- | :--- |
| `nepal` | `nepal` |
| `nigeria` | `africa_other` |
| `united kingdom` | `global` |
| `saudi arabia` | `asia_other` |
| `united states` | `global` |
| `india` | `asia_other` |
| `tanzania` | `africa_other` |
| `estonia` | `global` |
| `qatar` | `asia_other` |

*Note on distribution:* Because the majority of survey respondents are located in Nepal and Africa, these categories were designed to reflect this distribution.

### Industry Mapping
Industries are mapped into the following broad categories:
- `education`
- `tech`
- `public/government`
- `healthcare`
- `finance/trade`
- `none/other`
- `production/manufacturing`

*Note on `none/other`:* The `none/other` category merges "none" (which reflects unemployed respondents) with "other". Separating these two options resulted in categories that were too sparse to be statistically meaningful.

### AI Tools Mapping
AI tools are grouped into the following categories:
- `gen_ai/chatbot`
- `agriculture`
- `finance`
- `healthcare`
- `product/recommendation_system`
- `socialmedia/app`

*Mapping Details:*
- **`gen_ai/chatbot`**: Refers to general Large Language Model (LLM) services as well as image/video generation tools.
- **`socialmedia/app`**: Used for general social media platforms and apps utilizing an undisclosed type of AI.
- **`product/recommendation_system`**: A broader category separate from `socialmedia/app`, representing systems where AI is integrated but not specifically geared toward social media context.

### App Use AI Mapping
- **Drones**: Categorized under `travel/mobility`, as drones can represent multiple different use cases in practice.

### Education Mapping
- **Bachelors and Masters**: Grouped into a single category, as the "Masters" degree column was otherwise too sparse ("a dead column") to analyze independently.

### Residence Type Mapping
Residence categories are condensed into:
- `urban`
- `suburban`
- `rural`

*Specific mappings:*
- `municipal` is mapped to `suburban`.
- `city` is mapped to `urban`.