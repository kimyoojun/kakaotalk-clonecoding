<script>
  import InputBox from "$lib/components/InputBox.svelte"
  import Btn from "$lib/components/Btn.svelte"
  import axios from "axios";
  import { userName, accessToken, isLogin } from "$lib/store/login.js";

  let loginId = ""
  let loginPw = ""

  const loginBtn = async () => {
    const loginAPI = await axios.post("http://127.0.0.1:8000/auth/login", {"id": loginId, "pw": loginPw})
    
    if (loginAPI.status == 200){
      window.location.href="/app/friend"
      $userName = loginAPI.data[1].name
      $accessToken = loginAPI.data[1].token
      $isLogin = true
    }
  }

</script>
<div class="login-wrap">
  <div class="title-wrap">
    <h1 class="title">코코아톡</h1>
  </div>
  <div class="input-wrap">
    <InputBox inputName="아이디" bind:value={loginId}/>
    <InputBox inputName="비밀번호" bind:value={loginPw}/>
  </div>
  <div class="btn-wrap">
    <Btn btnName="로그인" onClick={loginBtn}/>
  </div>
  <div class="register-go-wrap">
    <a href="/register" class="register-go">회원가입</a>
  </div>
</div>

<style>
  .login-wrap {
    width: 100%;
    height: 100%;
    background-color: #f9e000;
  }

  .title-wrap {
    width: 100%;
    height: 300px;
    display: flex;
    align-items: flex-end;
  }

  .title {
    width: 100%;
    margin: 0;
    display: flex;
    justify-content: center;
    margin-bottom: 30px;
  }

  .input-wrap {
    width: 100%;
    height: 100px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-end;
  }

  .btn-wrap {
    width: 100%;
    height: 50px;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .register-go-wrap {
    width: 100%;
    height: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .register-go {
    text-decoration-line: none;
    color: rgb(60, 60, 60);
    font-size: 0.8rem;
  }
</style>
