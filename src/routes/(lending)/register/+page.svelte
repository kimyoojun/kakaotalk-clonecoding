<script>
  import InputBox from "$lib/components/InputBox.svelte"
  import Btn from "$lib/components/Btn.svelte"
  import axios from "axios";

  let registerEmail = ""
  let registerId = ""
  let registerName = ""
  let registerPw = ""
  let url = import.meta.env.KOKOAPI_HOST

  const registerbtn = async () => {
    console.log(registerName, registerEmail ,registerId ,registerPw)
    
    const registerAPI = await axios.post(url + "/auth/register", {"name": registerName, "email": registerEmail, "id": registerId, "pw": registerPw})
    if (registerAPI.status == 200) {
      window.location.href="/"
    }

  }
</script>
<div class="login-wrap">
  <div class="title-wrap">
    <h1 class="title">코코아톡</h1>
  </div>
  <div class="input-wrap">
    <InputBox inputName="이름" bind:value={registerName}/>
    <InputBox inputName="이메일" bind:value={registerEmail}/>
    <InputBox inputName="아이디" bind:value={registerId}/>
    <InputBox inputName="비밀번호" bind:value={registerPw}/>
  </div>
  <div class="btn-wrap">
    <Btn btnName="회원가입" onClick={registerbtn}/>
  </div>
  <div class="register-go-wrap">
    <a href="/" class="register-go">로그인</a>
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
    height: 200px;
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