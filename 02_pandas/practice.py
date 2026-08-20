import pandas as pd

df = pd.read_csv("datasets/netflix_titles.csv")

# =====================================================
# Module 01 - Pandas Practice
# Dataset: Netflix Movies & TV Shows
# =====================================================

# -----------------------------------------------------
# Q1
# Display the first 8 rows.
# -----------------------------------------------------

print(df.head(8))


# -----------------------------------------------------
# Q2
# Display the last 8 rows.
# -----------------------------------------------------

print(df.tail(8))


# -----------------------------------------------------
# Q3
# Print:
# - Shape
# - Column Names
# -----------------------------------------------------

print(df.shape)
print(df.columns)


# -----------------------------------------------------
# Q4
# Print:
# - Data Types
# - Dataset Summary
# -----------------------------------------------------

print(df.dtypes)
df.info()


# -----------------------------------------------------
# Q5
# Display only:
# title
# director
# country
# -----------------------------------------------------

print(df[["title", "director", "country"]])


# -----------------------------------------------------
# Q6
# Using iloc display:
# Rows 15–25
# Columns:
# title
# director
# release_year
# -----------------------------------------------------

print(df.iloc[15:26, [1, 2, 7]])


# =====================================================
# MEDIUM
# =====================================================

# -----------------------------------------------------
# Q7
# Display all Movies.
# -----------------------------------------------------

print(df[df["type"] == "Movie"])


# -----------------------------------------------------
# Q8
# Display all TV Shows.
# -----------------------------------------------------

print(df[df["type"] == "TV Show"])


# -----------------------------------------------------
# Q9
# Display titles released after 2018.
# Show:
# title
# release_year
# -----------------------------------------------------

print(df.loc[df["release_year"] > 2018, ["title", "release_year"]])


# -----------------------------------------------------
# Q10
# Display all content produced in India.
# Show:
# title
# type
# country
# -----------------------------------------------------

print(df.loc[df["country"] == "India", ["title", "type", "country"]])


# -----------------------------------------------------
# Q11
# Display Movies released in 2020.
# Show:
# title
# rating
# duration
# -----------------------------------------------------

print(
    df.loc[
        (df["type"] == "Movie") & (df["release_year"] == 2020),
        ["title", "rating", "duration"],
    ]
)


# -----------------------------------------------------
# Q12
# Using loc display:
# Rows 100–110
# Columns:
# title
# director
# rating
# -----------------------------------------------------

print(df.loc[100:110, ["title", "director", "rating"]])


# -----------------------------------------------------
# Q13
# Display every title where:
# rating == "TV-MA"
# -----------------------------------------------------

print(df.loc[df["rating"] == "TV-MA", ["title"]])


# =====================================================
# CHALLENGE
# =====================================================

# -----------------------------------------------------
# Q14
# Display:
# Movies
# released after 2015
# country == India
#
# Show:
# title
# release_year
# duration
# -----------------------------------------------------

print(
    df.query(
        "type == 'Movie' and release_year > 2015 and country == 'India'"
    )[["title", "release_year", "duration"]]
)


# -----------------------------------------------------
# Q15
# Display all titles released between
# 2010 and 2015 (inclusive).
# -----------------------------------------------------

print(
    df.query(
        "release_year >= 2010 and release_year <= 2015"
    )
)


# -----------------------------------------------------
# Q16
# Using ONLY iloc display:
#
# Rows:
# 50–70
#
# Columns:
# title
# release_year
# rating
# duration
# -----------------------------------------------------

print(df.iloc[50:71, [2, 7, 8, 9]])


# -----------------------------------------------------
# Q17
# Display every record where:
#
# type == "Movie"
# rating == "PG-13"
# -----------------------------------------------------

print(
    df.query(
        "type == 'Movie' and rating == 'PG-13'"
    )
)


# =====================================================
# MINI ANALYSIS
# =====================================================

# -----------------------------------------------------
# Q18
# How many Movies are present?
# -----------------------------------------------------

movie_count = len(df[df["type"] == "Movie"])
print("Movies:", movie_count)


# -----------------------------------------------------
# Q19
# How many TV Shows are present?
# -----------------------------------------------------

tv_show_count = len(df[df["type"] == "TV Show"])
print("TV Shows:", tv_show_count)


# -----------------------------------------------------
# Q20
# Which release year appears most frequently?
#
# Solved using only Python dictionaries.
# -----------------------------------------------------

freq = {}

for year in df["release_year"]:
    if year not in freq:
        freq[year] = 1
    else:
        freq[year] += 1

highest_key = max(freq, key=freq.get)

print("Most Frequent Release Year:", highest_key)