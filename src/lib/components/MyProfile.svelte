<script>
    export let myProfileImg = ""
    export let myProfileName = ""
    export let myProfileMessage = ""
</script>

<button class="myprofile-wrap">
    <div class="myimg-wrap">
        <img src={myProfileImg} alt="Profile" id="myprofile-img"/>
    </div>
    <div class="mystatus-message-wrap">
        <h4 class="myprofile-name">{myProfileName}</h4>
        <div class="mystatus-message">{myProfileMessage}</div>
    </div>
    <div class="mymulti-profile-wrap">
        <div class="mymulti-profile-btn">멀티프로필+</div>
    </div>
</button>

<style>
    .myprofile-wrap {
        width: 100%;
        height: 70px;
        display: flex;
        background-color: transparent;
        border: none;
        padding: 0;
    }

    .myprofile-wrap:hover {
        background-color: rgb(240, 240, 240);
    }

    .myimg-wrap {
        width: 90px;
        height: 70px;
        display: flex;
        align-items: center;
    }

    #myprofile-img {
        width: 50px;
        height: 50px;
        border-radius: 20px;
        margin-left: 20px;
    }

    .mystatus-message-wrap {
        height: 100%;
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
    }

    .myprofile-name {
        font-size: 0.9rem;
        margin: 0 0 3px 0;
    }

    .mystatus-message {
        font-size: 0.75rem;
    }

    .mymulti-profile-wrap {
        width: 120px;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .mymulti-profile-btn {
        font-size: 0.75rem;
        background-color: white;
        padding: 3px 8px;
        border-radius: 24px;
        border: 1px solid rgb(210, 210, 210);
    }
</style>