from pathlib import Path
from html import escape

# ============================================================
# CAREERLIX - INTERNATIONAL PRIVATE JOBS GENERATOR
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

# ============================================================
# 32 COUNTRIES
# ============================================================

COUNTRIES = [
    ("usa", "USA"),
    ("canada", "Canada"),
    ("uk", "United Kingdom"),
    ("australia", "Australia"),
    ("germany", "Germany"),
    ("uae", "United Arab Emirates"),
    ("saudi-arabia", "Saudi Arabia"),
    ("qatar", "Qatar"),
    ("singapore", "Singapore"),
    ("japan", "Japan"),
    ("new-zealand", "New Zealand"),
    ("netherlands", "Netherlands"),
    ("ireland", "Ireland"),
    ("portugal", "Portugal"),
    ("poland", "Poland"),
    ("malaysia", "Malaysia"),
    ("south-africa", "South Africa"),
    ("south-korea", "South Korea"),
    ("spain", "Spain"),
    ("sweden", "Sweden"),
    ("switzerland", "Switzerland"),
    ("thailand", "Thailand"),
    ("austria", "Austria"),
    ("belgium", "Belgium"),
    ("denmark", "Denmark"),
    ("finland", "Finland"),
    ("france", "France"),
    ("italy", "Italy"),
    ("norway", "Norway"),
    ("bahrain", "Bahrain"),
    ("oman", "Oman"),
    ("israel", "Israel"),
]


# ============================================================
# PAGE GENERATOR
# ============================================================

def create_private_page(folder, name):

    safe_name = escape(name)

    return f"""<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{safe_name} Private Jobs - Careerlix</title>

<meta name="description"
content="Explore private-sector jobs, corporate careers and multinational employment opportunities in {safe_name} with Careerlix.">

<link rel="icon" href="../../../../logo.png">

<style>

* {{
    box-sizing: border-box;
}}

body {{
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
    background: #f6f8fb;
    color: #111827;
}}

.site-header {{
    background: #ffffff;
    border-bottom: 1px solid #e5e7eb;
}}

.header-inner {{
    max-width: 1200px;
    margin: auto;
    padding: 18px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 25px;
}}

.logo {{
    display: flex;
    align-items: center;
    gap: 10px;
    text-decoration: none;
    color: #111827;
    font-size: 22px;
    font-weight: 700;
}}

.logo img {{
    width: 38px;
    height: 38px;
    object-fit: contain;
}}

.main-nav {{
    display: flex;
    flex-wrap: wrap;
    gap: 18px;
}}

.main-nav a {{
    color: #374151;
    text-decoration: none;
    font-weight: 600;
}}

.main-nav a:hover {{
    color: #0d6efd;
}}

.hero {{
    background: linear-gradient(135deg, #0d6efd, #063b8f);
    color: #ffffff;
    text-align: center;
    padding: 70px 20px;
}}

.hero-inner {{
    max-width: 900px;
    margin: auto;
}}

.badge {{
    display: inline-block;
    background: rgba(255,255,255,0.15);
    padding: 8px 14px;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: .5px;
}}

.hero h1 {{
    font-size: 44px;
    margin: 18px 0 12px;
}}

.hero p {{
    margin: auto;
    max-width: 800px;
    font-size: 18px;
    line-height: 1.7;
}}

.content {{
    max-width: 1200px;
    margin: 45px auto;
    padding: 0 20px;
}}

.breadcrumb {{
    display: flex;
    flex-wrap: wrap;
    gap: 9px;
    margin-bottom: 25px;
    color: #6b7280;
    font-size: 14px;
}}

.breadcrumb a {{
    color: #0d6efd;
    text-decoration: none;
}}

.card {{
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    overflow: hidden;
    box-shadow: 0 8px 28px rgba(0,0,0,.06);
}}

.card-top {{
    padding: 25px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    border-bottom: 1px solid #e5e7eb;
}}

.label {{
    display: inline-block;
    font-size: 12px;
    font-weight: 700;
    color: #0d6efd;
    letter-spacing: .5px;
}}

.card-top h2 {{
    margin: 8px 0 0;
    font-size: 28px;
}}

.country-badge {{
    background: #eef5ff;
    color: #0d6efd;
    padding: 9px 14px;
    border-radius: 30px;
    font-weight: 700;
    white-space: nowrap;
}}

.card-body {{
    padding: 28px;
}}

.card-body h3 {{
    margin-top: 0;
    font-size: 23px;
}}

.card-body > p {{
    color: #4b5563;
    line-height: 1.7;
}}

.jobs-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-top: 25px;
}}

.job-box {{
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 22px;
    background: #fafbfc;
}}

.job-box h4 {{
    margin: 0 0 9px;
    color: #111827;
    font-size: 17px;
}}

.job-box p {{
    margin: 0;
    color: #4b5563;
    line-height: 1.6;
    font-size: 14px;
}}

.notice {{
    margin-top: 28px;
    padding: 20px;
    border-radius: 12px;
    background: #eef6ff;
    border-left: 4px solid #1267d6;
}}

.notice strong {{
    color: #111827;
}}

.notice p {{
    margin-bottom: 0;
    color: #4b5563;
    line-height: 1.6;
}}

.footer {{
    margin-top: 50px;
    background: #111827;
    color: #d1d5db;
    padding: 28px 20px;
    text-align: center;
}}

.footer p {{
    margin: 0;
    font-size: 14px;
}}

@media (max-width: 800px) {{

    .header-inner {{
        flex-direction: column;
        align-items: flex-start;
    }}

    .jobs-grid {{
        grid-template-columns: 1fr;
    }}

    .card-top {{
        flex-direction: column;
        align-items: flex-start;
    }}

    .hero h1 {{
        font-size: 32px;
    }}

}}

</style>

</head>

<body>

<header class="site-header">

<div class="header-inner">

<a href="../../../../index.html" class="logo">

<img
src="../../../../logo.png"
alt="Careerlix Logo"
onerror="this.style.display='none'">

<span>Careerlix</span>

</a>

<nav class="main-nav">

<a href="../../../../index.html">Home</a>

<a href="../../../../jobs.html">Jobs</a>

<a href="../../../../index.html">
International &amp; Travel
</a>

<a href="../../../../notifications/notifications.html">
Notifications
</a>

<a href="../../../../legal/about.html">
About
</a>

<a href="../../../../legal/contact.html">
Contact
</a>

</nav>

</div>

</header>


<section class="hero">

<div class="hero-inner">

<span class="badge">
INTERNATIONAL PRIVATE JOBS
</span>

<h1>
{safe_name} Private Jobs
</h1>

<p>
Explore private company jobs, corporate careers,
multinational opportunities and employment options
in {safe_name}.
</p>

</div>

</section>


<main class="content">

<div class="breadcrumb">

<a href="../../../../index.html">
Home
</a>

<span>›</span>

<a href="../../../../index.html">
International &amp; Travel
</a>

<span>›</span>

<span>International Private Jobs</span>

<span>›</span>

<strong>{safe_name}</strong>

</div>


<section class="card">

<div class="card-top">

<div>

<span class="label">
PRIVATE SECTOR
</span>

<h2>
{safe_name} Private Jobs
</h2>

</div>

<span class="country-badge">
{safe_name}
</span>

</div>


<div class="card-body">

<h3>
Private Company Jobs in {safe_name}
</h3>

<p>
Find private-sector career opportunities,
corporate employment and multinational
company opportunities in {safe_name}.
</p>


<div class="jobs-grid">

<div class="job-box">

<h4>
Corporate Jobs
</h4>

<p>
Private company and corporate career
opportunities will be listed here.
</p>

</div>


<div class="job-box">

<h4>
Multinational Companies
</h4>

<p>
International and multinational company
opportunities will be added here.
</p>

</div>


<div class="job-box">

<h4>
Latest Vacancies
</h4>

<p>
Verified private-sector vacancies
will be published here.
</p>

</div>

</div>


<div class="notice">

<strong>
Private Job Updates
</strong>

<p>
Careerlix will add verified private-company
vacancies and career information to this page.
Always verify jobs through the official
employer before applying.
</p>

</div>

</div>

</section>

</main>


<footer class="footer">

<p>
© 2026 Careerlix. All Rights Reserved.
</p>

</footer>

</body>

</html>
"""


# ============================================================
# MAIN
# ============================================================

def main():

    print()
    print("=" * 65)
    print(" CAREERLIX INTERNATIONAL PRIVATE JOBS GENERATOR")
    print("=" * 65)
    print()

    created = 0
    skipped = 0

    for folder, name in COUNTRIES:

        private_dir = (
            BASE_DIR
            / "international-private-jobs"
            / folder
            / "private"
        )

        private_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        index_file = private_dir / "index.html"

        if index_file.exists():

            print(
                f"SKIPPED : {name} "
                "(index.html already exists)"
            )

            skipped += 1

        else:

            index_file.write_text(
                create_private_page(folder, name),
                encoding="utf-8"
            )

            print(
                f"CREATED : {name} "
                "→ private/index.html"
            )

            created += 1

    print()
    print("-" * 65)
    print(f"Created : {created}")
    print(f"Skipped : {skipped}")
    print(f"Total configured : {len(COUNTRIES)}")
    print("-" * 65)
    print()
    print("PRIVATE JOB STRUCTURE COMPLETE!")
    print()


if __name__ == "__main__":
    main()
