
pipeline 
{
   agent any

  

    stages
     { 
   
      stage('check branch') {
         when{
            not{
               anyof{
                  branch 'master'
                  branch 'staging'
                  branch 'development'
               }
            }
            
         }
            steps {
                echo "${env.BRANCH_NAME}"
               env.shouldBuild = false
            }//step end
       }//check branch
        
        stage('second')
        {
            when{
                    expression {
                        return env.shouldBuild != "false"
                    }
            }//when
        }
            
        
    }//stage end
}
