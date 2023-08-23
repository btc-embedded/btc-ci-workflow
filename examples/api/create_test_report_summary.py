import datetime
import os


# results should be a list of entries with the fields:
#   projectName, duration (seconds), statementCoverage, mcdcCoverage,
#   testResult, eppPath, reportPath
def create_test_report_summary(results, report_title='BTC Test Report Summary', report_name='BTCTestReportSummary.html'):
    total_duration = sum(project['duration'] for project in results)
    overall_status = "ERROR" if any(project["testResult"] == "ERROR" for project in results) else ("FAILED" if any(project["testResult"] == "FAILED" for project in results) else "PASSED")

    with open('btc_summary_report.template') as f:
        html_template = f.read()

    projects_string = ''
    for result in results:
        projects_string += get_project_string(result) + '\r\n'

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

    # Write the HTML to a file
    with open(report_name, "w") as f:
        f.write(final_html)

#
# ----------------------------- Sub-functions -----------------------------
#

def get_project_string(result):
    """
    - projectName      : can be eppName without extension
    - testResult       : PASSED / FAILED / NO_VERDICT / ERROR
    - statementCoverage
    - mcdcCoverage
    - reportPath       : path to project report.html
    - eppPath          : path to project.epp
    - eppName          : name of the project.epp (incl. extension) -> eppPath basename
    - duration         : duration in the form hh:mm:ss
    - statusIconClass  : icon-sdc (green), icon-wdc (yellow/orange), icon-edc (red)
    - statusMessage    : message on mouseOver of the status icon
    """
    template = '<tr><td><span class="{statusIconClass}" title="{statusMessage}"> </span></td><td><a href="{reportPath}">{projectName}</a></td><td>{statementCoverage}% Statement, {mcdcCoverage}% MC/DC</td><td><a href="{eppPath}">{eppName}</a></td><td>{duration}</td><td><div class="result_container"><div class="{testResult}"/><b>{testResult}</b></div></td></tr>'
    # Fill in the HTML template with the data
    project_html_entry = template.format(
        projectName = result["projectName"],
        testResult = result["testResult"],
        statementCoverage = result["statementCoverage"],
        mcdcCoverage = result["mcdcCoverage"],
        reportPath = result["reportPath"],
        eppPath = result["eppPath"],
        eppName = os.path.basename(result["eppPath"]),
        duration = seconds_to_hms(result["duration"]),
        statusIconClass = ('icon-sdc' if result["testResult"] == 'PASSED' else 'icon-wdc' if result["testResult"] == 'FAILED' else 'icon-edc'),
        statusMessage = result["testResult"]
    )
    return project_html_entry


def seconds_to_hms(seconds):
    """converts from 42343 (seconds) to 11:45:43 (hh:mm:ss)"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"