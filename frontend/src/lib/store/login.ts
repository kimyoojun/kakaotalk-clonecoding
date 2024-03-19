import { writable } from 'svelte/store'

export let accessToken = writable('')
export let userName = writable('')
export let isLogin = writable(false)

// export function getStoredValues() {
//   if (typeof window !== 'undefined') {
//     accessToken.subscribe((value) => {
//       if (value !== null) {
//         localStorage.setItem('accessToken', value)
//       }
//     })

//     userName.subscribe((value) => {
//       if (value !== null) {
//         localStorage.setItem('userName', value)
//       }
//     })

//     isLogin.subscribe((value) => {
//       if (value !== null) {
//         localStorage.setItem('isLogin', value.toString())
//       }
//     })
//     let storedAccessToken = localStorage.getItem('accessToken')
//     let storedUserName = localStorage.getItem('userName') || ''
//     let storedIsLogin = localStorage.getItem('isLogin') || ''

//     if (storedAccessToken) accessToken.set(storedAccessToken)
//     if (storedUserName) userName.set(storedUserName)
//     if (storedIsLogin) isLogin.set(storedIsLogin === 'true')
//   }
// }

// getStoredValues()

if (typeof window !== 'undefined') {
  let storedAccessToken = localStorage.getItem('accessToken')
  let storeduserName = localStorage.getItem('userName')
  let storedIsLogin = localStorage.getItem('isLogin')

  if (storedAccessToken) {
    accessToken.set(storedAccessToken)
  }

  if (storeduserName) {
    userName.set(storeduserName)
  }

  if (storedIsLogin) {
    isLogin.set(storedIsLogin == 'true')
  }
}
