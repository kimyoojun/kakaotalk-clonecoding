<script>
  import { isToggleStore } from "$lib/stores/friendAdd";
  import axios from "axios";

  let searchFriend = ""
  let userIform = ""

  const handleButtonClick = () => {
    $isToggleStore.friendAdd = !$isToggleStore.friendAdd
  }

  const friendAdd = async (event) => {
    if (event.key === "Enter") {
      console.log(searchFriend,"클릭")
      const friendselect = await axios.post("http://127.0.0.1:8000/user/select", {"name": searchFriend})
      console.log(friendselect.data.name)
      userIform = friendselect.data.name
    }
  }

  const friendAddBtn = async () => {
    console.log("추가")
    const friendadd = await axios.post("http://127.0.0.1:8000/user/add", {"my_name": localStorage.getItem('username'), "user_name": userIform})
  }

</script>

<div class="add-model-bg">
  <button class="full-model-btn" on:click={handleButtonClick}/>
  <div class="friend-add-wrap">
    <div class="add-title-wrap">
      <h1>친구 추가</h1>
    </div>
    <div class="add-search-wrap">
      <input class="add-search" placeholder="친구 이름" bind:value={searchFriend} on:keydown={friendAdd}/>
    </div>
    <div class="friend-list-wrap">
      {#if userIform}
        <div class="user-wrap">
          <img src="/icons/초전도치.png" alt="Profile"/>
          <div class="user-name">{userIform}</div>
          <button on:click={friendAddBtn}>추가</button>
        </div>
      {/if}
    </div>
  </div>
</div>

<style>
  .add-model-bg {
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    position: fixed;
    left: 0;
    top: 0;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .full-model-btn {
    width: 100%;
    height: 100%;
    border: none;
    background-color: transparent;
    position: absolute;
  }

  .friend-add-wrap {
    width: 70%;
    height: 50%;
    background-color: white;
    z-index: 99;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .add-title-wrap {
    width: 100%;
    height: 40px;
    display: flex;
    align-items: flex-end;
    border-bottom: 1px solid black;
    padding-bottom: 5px;
  }

  .add-title-wrap h1 {
    font-size: 1.2rem;
    margin: 0 0 0 20px;
  }

  .add-search-wrap {
    width: 100%;
    height: 60px;
    display: flex;
    align-items: flex-end;
    justify-content: center;
  }

  .add-search {
    width: 80%;
    height: 30px;
    border: none;
    border-bottom: 1px solid black;
    outline: none;
    margin-bottom: 10px;
  }

  .friend-list-wrap {
    width: 100%;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .user-wrap {
    width: 90%;
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .user-wrap img {
    height: 35px;
    border-radius: 10px;
  }

  .user-name {
    margin-left: 10px;
    flex-grow: 1;
    font-size: 0.9rem;
  }

  .user-wrap button {
    border: none;
    width: 40px;
    height: 30px;
    background-color: rgb(229, 229, 229);
  }
</style>