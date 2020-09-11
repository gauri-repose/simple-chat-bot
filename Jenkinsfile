dev shouldBuild = false
pipeline 
{
   agent any

  

    stages
     { 
   
      stage('check branch') {
         when{
            not{
               anyOf{
                  branch 'master'
                  branch 'staging'
                  branch 'development'
               }
            }
            
         }
            steps {
                echo "${env.BRANCH_NAME}"
               script{
                 env.shouldBuild = false
               }
             }//step end
       }//check branch
        
        stage('second')
        {
            when{
                    expression {
                        return env.shouldBuild != "false"
                    }
            }//when
           steps{
           echo "inside second step"
           }
           
        }
            
        
    }//stage end
}
