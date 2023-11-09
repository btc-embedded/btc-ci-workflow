/* 
 * Example for BTC test of a TargetLink model with GitLab CI
 *
 * - This example should provide some initial directions.
 * - It is untested and needs to be adapted to work
 */
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
                bat "python examples/test_workflow_ec.py \"${WORKSPACE}/examples/EmbeddedCoderAutosar_SHC/shc_ec_ar.epp\""
            }
        }

        stage('Publish Report') {
            steps {
                // Publish the HTML report
                publishHTML([
                    reportDir: 'examples/EmbeddedCoderAutosar_SHC',
                    reportFiles: 'report.html',
                    reportName: 'BTC Test Report'
                ])
            }
        }
    }
}
