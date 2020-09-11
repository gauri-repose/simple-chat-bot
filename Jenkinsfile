def shouldBuild = false
pipeline 
{
   agent any

  

    stages
     { 
   
      stage('check branch') {

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
