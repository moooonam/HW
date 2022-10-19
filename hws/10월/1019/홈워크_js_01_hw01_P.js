// 1번
const nums = [1,2,3,4,5,6,7,8]

for (const i = 0; i < nums.length; i++) {
  console.log()
}

// for (const i = 0; i < nums.length; i++) {
//                                     ^

// TypeError: Assignment to constant variable.

// 답: const로 변수를 선언하면 재 할당이 불가능 하기 때문에 let으로 바꿔주어야 함

for (let i = 0; i < nums.length; i++) {
    console.log()
  }

// 2번
// in을 of으로 바꾼다
for (num of nums) {
  console.log(num, typeof num)
}

// 0 string
// 1 string
// 2 string
// 3 string
// 4 string
// 5 string
// 6 string
// 7 string
