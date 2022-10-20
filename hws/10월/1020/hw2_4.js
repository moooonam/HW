const inputs = [
    [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
    [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
    [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
  ]

  function solution(K, N, M, chargers) {
    // solution 함수 완성
    let count = 0
    let my_p = 0
    while (my_p + K < N) {
        for (let i = K; i > 0; i--){
            if ((my_p + i) in chargers) {
                my_p += i
                count += 1
                break
            } else {
                count = 0
                break
            }
        }
    }
    return console.log(count)
  }
  
  for (const input of inputs) {
    solution(input[0], input[1], input[2], input[3])
  }