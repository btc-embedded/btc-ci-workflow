// Pipeline for the BTC tests via Python & BTC Rest API
pipeline {
    // run on an agent with BTC, Matlab and Python
    agent { label "BTC && MATLAB && PYTHON" }


    stages {
        stage('Checkout') {
            steps {
                // Check out the code from the git repo specified in the pipeline config
                checkout scm
            }
        }

        stage('Prepare Environment') {
            steps {
                // Install Python and dependencies from requirements.txt
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run the python script to invoke tests
                bat "python examples/test_workflow_sl.py \"${WORKSPACE}/examples/Simulink_PWC/pwc_sl.epp\""
            }
        }

        stage('Publish Report') {
            steps {
                // Publish the HTML report
                publishHTML([
                    reportDir: 'examples/Simulink_PWC',
                    reportFiles: 'report.html',
                    reportName: 'BTC Test Report'
                ])
            }
        }
    }
}
