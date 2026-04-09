# 별 찍기 - 11
''' 3 6 12 24 48
  * 5                      
 * * 4                      
***** 3

     * 5                      
    * * 4                      
   ***** 3
  *     * 2                  
 * *   * * 1                  
***** ***** 0     6

           *  23                      
          * * 22                      
         *****  21                     3
        *     *  20                   
       * *   * *  19                  
      ***** *****  18                 6
     *           *   17               
    * *         * *    16             
   *****       *****     15           
  *     *     *     *      14         
 * *   * *   * *   * *    13          
***** ***** ***** *****  12   
                       *  23                      
                      * * 22                      
                     *****  21                     3
                    *     *  20                   
                   * *   * *  19                  
                  ***** *****  18                 6
                 *           *   17               
                * *         * *    16             
               *****       *****     15           
              *     *     *     *      14         
             * *   * *   * *   * *    13          
            ***** ***** ***** *****  12           12
           *                       *  11          
          * *                     * *   10        
         *****                   *****  9        
        *     *                 *     *  8       
       * *   * *               * *   * *  7      
      ***** *****             ***** *****  6     
     *           *           *           *  5    
    * *         * *         * *         * *  4   
   *****       *****       *****       *****  3  
  *     *     *     *     *     *     *     *  2 
 * *   * *   * *   * *   * *   * *   * *   * *  1
***** ***** ***** ***** ***** ***** ***** *****  0    24
'''
N = int(input())
tree = [[" ", " ", "*", " ", " "],
        [" ", "*", " ", "*", " "],
        ["*", "*", "*", "*", "*"]]

def check(degree, before):
    after = [[" "]*(degree*4 - 1) for _ in range(2*degree)]
    for i in range(degree):
        after[i][degree:degree*2+degree-1] = before[i]
    
    k = 0
    for i in range(degree, 2*degree):
        after[i][:2*degree] = before[k]
        after[i][2*degree:2*degree+len(before[k])] = before[k]
        k += 1
        
    if 2*degree == N:
        return after

    return check(2*degree, after)

answ = ''
if N == 3:
    answ = tree
else:
    answ = check(3, tree)

for row in answ:
    for ele in row:
        print(ele, end='')
    print()

# 참고자료 : https://hongcoding.tistory.com/90