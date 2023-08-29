import datetime
import os

thisfile = os.path.abspath(__file__).replace('\\', '/')
BTC_SUMMARY_REPORT_TEMPLATE = os.path.join(os.path.dirname(thisfile), 'btc_summary_report.template')

# 
# ----------------------------- Main-function -----------------------------
# 
def create_test_report_summary(results, report_title='BTC Test Report Summary', report_name='BTCTestReportSummary.html'):
    """
    Takes a list of individual results and creates a summary report from it.
    
    The results objects are expected to contain the following fields:
    - projectName
    - duration (integer indicating the duration in seconds)
    - statementCoverage
    - mcdcCoverage
    - testResult (PASSED / FAILED / ERROR / SKIPPED)
    - eppPath (path to the *.epp file)
    - reportPath (path to the project's html report)
    """
    # aggregate total_duration and overall_status
    total_duration = sum(project['duration'] for project in results)
    overall_status = "ERROR" if any(project["testResult"] == "ERROR" for project in results) else ("FAILED" if any(project["testResult"] == "FAILED" for project in results) else "PASSED")

    # import html template
    with open(BTC_SUMMARY_REPORT_TEMPLATE) as f:
        html_template = f.read()

    # prepare projects_string, containing info for all projects
    projects_string = ''
    for result in results:
        projects_string += get_project_string(result) + '\r\n'

    # fill placeholders in template
    final_html = html_template.replace('__title__', report_title)\
                              .replace('__creator__', os.getenv('USERNAME') or os.getlogin())\
                              .replace('__timestamp__', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))\
                              .replace('__totalDuration__', seconds_to_hms(total_duration))\
                              .replace('__averageDuration__', seconds_to_hms(total_duration // len(results)))\
                              .replace('__overallStatus__', overall_status)\
                              .replace('__numberOfProjects__', str(len(results)))\
                              .replace('__numberOfProjectsPassed__', str(sum(1 for project in results if project["testResult"] == "PASSED")))\
                              .replace('__numberOfProjectsFailed__', str(sum(1 for project in results if project["testResult"] == "FAILED")))\
                              .replace('__projects__', projects_string)

    # Write the final HTML file
    with open(report_name, "w") as f:
        f.write(final_html)


#
# ----------------------------- Sub-functions -----------------------------
#

def get_project_string(result):
    # we need to replace the following placeholders:
    # - projectName      : can be eppName without extension
    # - testResult       : PASSED / FAILED / NO_VERDICT / ERROR
    # - statementCoverage
    # - mcdcCoverage
    # - reportPath       : path to project report.html
    # - eppPath          : path to project.epp
    # - eppName          : name of the project.epp (incl. extension) -> eppPath basename
    # - duration         : duration in the form hh:mm:ss
    template = '<tr><td><span class="{statusIconClass}" title="{statusMessage}"> </span></td><td><a href="{reportPath}">{projectName}</a></td><td>{statementCoverage}% Statement, {mcdcCoverage}% MC/DC</td><td><a href="{eppPath}">{eppName}</a></td><td>{duration}</td><td><div class="result_container"><div class="{testResult}"/><b>{testResult}</b></div></td></tr>'
    # Fill in the HTML template with the data
    project_html_entry = template.format(
        projectName = result["projectName"],
        testResult = result["testResult"],
        statementCoverage = f'{result["statementCoverage"]:.2f}',
        mcdcCoverage = f'{result["mcdcCoverage"]:.2f}',
        reportPath = result["reportPath"],
        eppPath = result["eppPath"],
        eppName = os.path.basename(result["eppPath"]),
        duration = seconds_to_hms(result["duration"]),
        statusIconClass = ('icon-sdc' if result["testResult"] == 'PASSED' else 'icon-wdc' if result["testResult"] == 'FAILED' else 'icon-edc'),
        statusMessage = result["testResult"]
    )
    return project_html_entry


def seconds_to_hms(seconds):
    """Converts a seconds value (like 42343) into an hh:mm:ss value (like 11:45:43)"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"