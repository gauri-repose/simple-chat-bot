def shouldBuild = false
def replace_file_folder="MYANDROID"
def branch_name = ""
pipeline 
{
    //agent any
    agent {
        docker { image 'android-30:0.1' 
                 args '-u root:root'
        }
    }
    environment {
        APP_ID     =    credentials('FB_DEVOPS_APP_ID')
        JENKINS_CHANNEL = "jenkins_android"
    }

    stages
     { 
        // stage('Download project') {
        //     steps {
        //   checkout changelog: false, poll: false, scm: [$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'GITHUB_SR', url: 'https://github.com/ShubhamRasal/simple-chat-bot.git']]]            }
        // }
        stage('Init') {
            steps {
                script {
                    lastCommitInfo = sh(script: "git log -1", returnStdout: true).trim()
                    commitContainsSkip = sh(script: "git log -1 | grep 'skip ci'", returnStatus: true)
                                       slackMessage = "*${env.JOB_NAME}* *${env.BRANCH_NAME}* received a new commit. \nHere is commmit info: ${lastCommitInfo}"
                    
                    //send slack notification of new commit
                    slack_send(slackMessage,"${env.JENKINS_CHANNEL}")
                  
                    //if commit message contains skip ci
                    if(commitContainsSkip == 0) {
                        skippingText = "Skipping commit."
                        env.shouldBuild = false
                        currentBuild.result = "NOT_BUILT"
                        slack_send("Skipping this commit for build operation.","${env.JENKINS_CHANNEL}")
                    }
                }
            }//step end
        }
        //build 

        //download neccessary files like dependency and properties file
        // stage('download necessary files'){
        //     steps{
        //       dir("files")
        //        {
        //          git credentialsId: 'GITHUB_SR', url: 'https://github.com/ShubhamRasal/DEVOPS_FILES.git'               
        //        }
        //     }
        // }
    
        stage('check branch') {
            steps {
                script {
                    branch_name = "${env.BRANCH_NAME}"
                   // echo branch_name
                    if(branch_name == "master"){
                           echo branch_name
                        
                    }else if(branch_name == "dev"){
                       
                          echo branch_name  
                    }else if(branch_name == "staging"){
                        
                           echo branch_name
                    }else if(branch_name == "null"){
                        
                        echo branch_name
                    }
                }
            }//step end
            }
            
        
    }//stage end
}

def slack_send(slackMessage,channel="jenkins",messageColor="good")
{
    slackSend channel: channel , color: messageColor, message: slackMessage
}