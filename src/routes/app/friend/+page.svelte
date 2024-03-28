<script>
    import MyProfile from "$lib/components/MyProfile.svelte";
    import Profile from "$lib/components/Profile.svelte";
    import { onMount } from "svelte";
    import FriendAddModel from "$lib/components/FriendAddModel.svelte"
    import { isToggleStore } from "$lib/stores/friendAdd";
    import axios from "axios"

    let username = ""
    let usertoken = ""
    let friendsList = ""
    let myuuid = ""
    const url = import.meta.env.KOKOATALK_HOST


    onMount(async () => {
        username = localStorage.getItem('username')
        usertoken = localStorage.getItem('token')
        myuuid = localStorage.getItem('myuuid')

        const friendList = await axios.post(url + "friendlist",{"my_token": usertoken})

        friendsList = friendList.data
    })

    const friendAddClick = () => {
        $isToggleStore.friendAdd = !$isToggleStore.friendAdd
    }

    const chatMove = async (i) => {
        const chatting = await axios.post(url + "message", {"my_uuid": myuuid, "user_name": friendsList[i]})
        localStorage.setItem('chatuseruuid', chatting.data[1].uuid)  
        localStorage.setItem('chatuuid', chatting.data[2])
        console.log(chatting)
        window.location.href=url + "chatting"
        
    }
</script>

<div class="friend-wrap">
    <div class="friend-top-wrap">
        <div class="friend-top-element">
            <h2 class="friend-title">친구</h2>
        </div>
        <div class="friend-top-element">
            <div class="friend-icon-wrap">
                <img src="/icons/searched.svg" alt="Icon" title="통합검색" id="friend-top-icon"/>
            </div>
            <button class="friend-icon-wrap" on:click={friendAddClick}>
                <img src="/icons/plus-circle.svg" alt="Icon" title="친구 추가" id="friend-top-icon"/>
            </button>
        </div>
    </div>
    <MyProfile myProfileImg="/icons/초전도치.png" myProfileName={username} myProfileMessage="출근시러 퇴근조아"/>
    {#each friendsList as friend, i}
        <button class="profile-wrap" on:click={() => chatMove(i)}>
            <Profile profileImg="/icons/초전도치.png" profileName={friend} profileMessage="권모술수"/>
        </button>
    {/each}
</div>
{#if $isToggleStore.friendAdd}
    <FriendAddModel/>
{/if}

<style>
    .friend-wrap {
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
    }

    .friend-top-wrap {
        display: flex;
        justify-content: space-between;
        width: 100%;
        height: 70px;
    }

    .friend-top-element {
        display: flex;
        width: auto;
        height: auto;
        padding: 30px 20px;
    }

    .friend-icon-wrap {
        width: 30px;
        height: 30px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        cursor: pointer;
        border: none;
        background-color: transparent;
    }

    #friend-top-icon {
        width: 25px;
    }

    .friend-title {
        margin: 0;
    }

    .profile-wrap {
        width: auto;
        height: auto;
        background-color: transparent;
        border: none;
        padding: 0;
    }
</style>