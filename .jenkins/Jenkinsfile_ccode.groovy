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
                bat "python examples/test_workflow_c.py \"${WORKSPACE}/examples/CCode_SPA/spa_c.epp\""
            }
        }

        stage('Publish Report') {
            steps {
                // Publish the HTML report
                publishHTML([
                    reportDir: 'examples/CCode_SPA',
                    reportFiles: 'report.html',
                    reportName: 'BTC Test Report'
                ])
            }
        }
    }
}
