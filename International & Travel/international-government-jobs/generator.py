from pathlib import Path
from html import escape

# ============================================================
# CAREERLIX - INTERNATIONAL GOVERNMENT JOBS GENERATOR
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

# ============================================================
# FINAL 32 COUNTRIES
# ============================================================

COUNTRIES = [
    {
        "folder": "usa",
        "name": "USA",
        "level": "Federal",
        "level_folder": "federal",
        "government": "United States Federal Government",
    },
    {
        "folder": "canada",
        "name": "Canada",
        "level": "Federal",
        "level_folder": "federal",
        "government": "Government of Canada",
    },
    {
        "folder": "uk",
        "name": "United Kingdom",
        "level": "Central",
        "level_folder": "central",
        "government": "UK Central Government",
    },
    {
        "folder": "australia",
        "name": "Australia",
        "level": "Federal",
        "level_folder": "federal",
        "government": "Australian Federal Government",
    },
    {
        "folder": "germany",
        "name": "Germany",
        "level": "Federal",
        "level_folder": "federal",
        "government": "Federal Government of Germany",
    },
    {
        "folder": "uae",
        "name": "United Arab Emirates",
        "level": "Federal",
        "level_folder": "federal",
        "government": "UAE Federal Government",
    },
    {
        "folder": "saudi-arabia",
        "name": "Saudi Arabia",
        "level": "National",
        "level_folder": "national",
        "government": "Government of Saudi Arabia",
    },
    {
        "folder": "qatar",
        "name": "Qatar",
        "level": "National",
        "level_folder": "national",
        "government": "Government of Qatar",
    },
    {
        "folder": "singapore",
        "name": "Singapore",
        "level": "National",
        "level_folder": "national",
        "government": "Government of Singapore",
    },
    {
        "folder": "japan",
        "name": "Japan",
        "level": "National",
        "level_folder": "national",
        "government": "Government of Japan",
    },
    {
        "folder": "new-zealand",
        "name": "New Zealand",
        "level": "National",
        "level_folder": "national",
        "government": "Government of New Zealand",
    },
    {
        "folder": "netherlands",
        "name": "Netherlands",
        "level": "National",
        "level_folder": "national",
        "government": "Government of the Netherlands",
    },

    # 20 additional countries
    {
        "folder": "ireland",
        "name": "Ireland",
        "level": "Central",
        "level_folder": "central",
        "government": "Government of Ireland",
    },
    {
        "folder": "portugal",
        "name": "Portugal",
        "level": "National",
        "level_folder": "national",
        "government": "Government of Portugal",
    },
    {
        "folder": "poland",
        "name": "Poland",
        "level": "National",
        "level_folder": "national",
        "government": "Government of Poland",
    },
    {
        "folder": "malaysia",
        "name": "Malaysia",
        "level": "Federal",
        "level_folder": "federal",
        "government": "Government of Malaysia",
    },
    {
        "folder": "south-africa",
        "name": "South Africa",
        "level": "National",
        "level_folder": "national",
        "government": "Government of South Africa",
    },
    {
        "folder": "south-korea",
        "name": "South Korea",
        "level": "National",
        "level_folder": "national",
        "government": "Government of South Korea",
    },
    {
        "folder": "spain",
        "name": "Spain",
        "level": "National",
        "level_folder": "national",
        "government": "Government of Spain",
    },
    {
        "folder": "sweden",
        "name": "Sweden",
        "level": "National",
        "level_folder": "national",
        "government": "Government of Sweden",
    },
    {
        "folder": "switzerland",
        "name": "Switzerland",
        "level": "Federal",
        "level_folder": "federal",
        "government": "Swiss Federal Government",
    },
    {
        "folder": "thailand",
        "name": "Thailand",
        "level": "National",
        "level_folder": "national",
        "government": "Government of Thailand",
    },
    {
        "folder": "austria",
        "name": "Austria",
        "level": "Federal",
        "level_folder": "federal",
        "government": "Federal Government of Austria",
    },
    {
        "folder": "belgium",
        "name": "Belgium",
        "level": "Federal",
        "level_folder": "federal",
        "government": "Federal Government of Belgium",
    },
    {
        "folder": "denmark",
        "name": "Denmark",
        "level": "National",
        "level_folder": "national",
        "government": "Government of Denmark",
    },
    {
        "folder": "finland",
        "name": "Finland",
        "level": "National",
        "level_folder": "national",
        "government": "Government of Finland",
    },
    {
        "folder": "france",
        "name": "France",
        "level": "National",
        "level_folder": "national",
        "government": "Government of France",
    },
    {
        "folder": "italy",
        "name": "Italy",
        "level": "National",
        "level_folder": "national",
        "government": "Government of Italy",
    },
    {
        "folder": "norway",
        "name": "Norway",
        "level": "National",
        "level_folder": "national",
        "government": "Government of Norway",
    },
    {
        "folder": "bahrain",
        "name": "Bahrain",
        "level": "National",
        "level_folder": "national",
        "government": "Government of Bahrain",
    },
    {
        "folder": "oman",
        "name": "Oman",
        "level": "National",
        "level_folder": "national",
        "government": "Government of Oman",
    },
    {
        "folder": "israel",
        "name": "Israel",
        "level": "National",
        "level_folder": "national",
        "government": "Government of Israel",
    },
]


# ============================================================
# PAGE TEMPLATE
# ============================================================

def create_country_page(country):
    folder = country["folder"]
    name = escape(country["name"])
    level = escape(country["level"])
    government = escape(country["government"])

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>{name} Government Jobs | Careerlix</title>

    <meta name="description"
          content="{name} government jobs, federal and national government vacancies, careers and official recruitment information.">

    <link rel="stylesheet" href="../../../../style.css">
</head>

<body>

<header class="site-header">

    <div class="header-inner">

        <a href="../../../../index.html" class="logo">
            <img src="../../../../logo.png"
                 alt="Careerlix Logo"
                 onerror="this.style.display='none'">
            <span>Careerlix</span>
        </a>

        <nav class="main-nav">
            <a href="../../../../index.html">Home</a>
            <a href="../../../../jobs.html">Jobs</a>
            <a href="../../../../International%20%26%20Travel/index.html">
                International &amp; Travel
            </a>
            <a href="../../../../notifications/index.html">
                Notifications
            </a>
            <a href="../../../../about.html">About</a>
            <a href="../../../../contact.html">Contact</a>
        </nav>

    </div>

</header>


<main>

    <section class="hero-section">

        <div class="hero-content">

            <span class="badge">
                INTERNATIONAL GOVERNMENT JOBS
            </span>

            <h1>
                {name} Government Jobs
            </h1>

            <p>
                Explore {name} {level.lower()} government career
                opportunities and official recruitment information.
            </p>

        </div>

    </section>


    <section class="content-section">

        <div class="container">

            <div class="breadcrumb">
                <a href="../../../../index.html">Home</a>
                <span>›</span>
                <a href="../../../../International%20%26%20Travel/index.html">
                    International &amp; Travel
                </a>
                <span>›</span>
                <span>International Government Jobs</span>
                <span>›</span>
                <strong>{name}</strong>
            </div>


            <div class="page-card">

                <div class="card-header">

                    <div>
                        <span class="small-label">
                            GOVERNMENT
                        </span>

                        <h2>
                            {government}
                        </h2>
                    </div>

                    <span class="level-badge">
                        {level}
                    </span>

                </div>


                <div class="card-body">

                    <h3>
                        {name} Government Jobs
                    </h3>

                    <p>
                        This page is dedicated to government employment
                        opportunities in {name}.
                    </p>

                    <p>
                        Official government vacancies and recruitment
                        information will be added here.
                    </p>


                    <div class="info-grid">

                        <div class="info-box">
                            <span>Country</span>
                            <strong>{name}</strong>
                        </div>

                        <div class="info-box">
                            <span>Government Level</span>
                            <strong>{level}</strong>
                        </div>

                        <div class="info-box">
                            <span>Vacancies</span>
                            <strong>Coming Soon</strong>
                        </div>

                    </div>


                    <div class="notice-box">

                        <strong>Official Vacancy Updates</strong>

                        <p>
                            Careerlix will publish verified government
                            job opportunities and recruitment information
                            on this page.
                        </p>

                    </div>

                </div>

            </div>

        </div>

    </section>

</main>


<footer class="site-footer">

    <div class="container">

        <p>
            © 2026 Careerlix. All Rights Reserved.
        </p>

    </div>

</footer>


</body>
</html>
"""

    return page


# ============================================================
# MAIN GENERATOR
# ============================================================

def main():

    print()
    print("=" * 60)
    print(" CAREERLIX INTERNATIONAL GOVERNMENT JOB GENERATOR")
    print("=" * 60)
    print()

    created = 0
    skipped = 0

    for country in COUNTRIES:

        country_dir = (
            BASE_DIR
            / country["folder"]
            / "government"
            / country["level_folder"]
        )

        country_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        index_file = country_dir / "index.html"

        if index_file.exists():

            print(
                f"SKIPPED : {country['name']} "
                f"(index.html already exists)"
            )

            skipped += 1

        else:

            index_file.write_text(
                create_country_page(country),
                encoding="utf-8"
            )

            print(
                f"CREATED : {country['name']} → "
                f"government/{country['level_folder']}/index.html"
            )

            created += 1


    print()
    print("-" * 60)
    print(f"Created : {created}")
    print(f"Skipped : {skipped}")
    print(f"Total configured : {len(COUNTRIES)}")
    print("-" * 60)
    print()
    print("DONE!")
    print()


if __name__ == "__main__":
    main()