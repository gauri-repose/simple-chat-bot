def shouldBuild = true
pipeline 
{
   agent any

  

    stages
     { 
   
      stage('check branch') {

            steps {
                echo "${env.BRANCH_NAME}"
               script{
                  if (env.BRANCH_NAME != 'master' && env.BRANCH_NAME != 'staging' && env.BRANCH_NAME != 'development') {
                      echo 'This is not master or staging'
                   env.shouldBuild = false
               }  
               }//script
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
