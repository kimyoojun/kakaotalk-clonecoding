<script>
    export let profileImg = ""
    export let profileName = ""
    export let profileMessage = ""
</script>

<div class="profile-wrap">
    <div class="img-wrap">
        <img src={profileImg} alt="Profile" id="profile-img"/>
    </div>
    <div class="status-message-wrap">
        <h4 class="profile-name">{profileName}</h4>
        <div class="status-message">{profileMessage}</div>
    </div>
</div>

<style>
    .profile-wrap {
        width: 100%;
        height: 50px;
        display: flex;
    }

    .profile-wrap:hover {
        background-color: rgb(240, 240, 240);
    }
    
    .img-wrap {
        width: 70px;
        height: 100%;
        display: flex;
        align-items: center;
    }

    #profile-img {
        width: 40px;
        height: 40px;
        border-radius: 16px;
        margin-left: 20px;
    }

    .status-message-wrap {
        height: 100%;
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
    }

    .profile-name {
        font-size: 0.85rem;
        margin: 0;
    }

    .status-message {
        font-size: 0.7rem;
    }
</style>