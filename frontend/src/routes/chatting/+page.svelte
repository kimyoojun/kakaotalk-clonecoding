<script>
    import TopIcon from "$lib/components/chatting/TopIcon.svelte";
    import BottomIcon from "$lib/components/chatting/BottomIcon.svelte";

    export let texts = ""
</script>

<div class="chatting-wrap">
    <div class="chatting-top-wrap">
        <div class="chatting-img-wrap">
            <img src="/icons/초전도치.png" alt="프로필사진" id="chatting-img"/>
        </div>
        <div class="chatting-title-wrap">
            <div class="chatting-title">현석</div>
        </div>
        <div class="chatting-icon-wrap">
            <TopIcon chatTopIcon="/icons/searched.svg"/>
            <TopIcon chatTopIcon="/icons/phone.svg"/>
            <TopIcon chatTopIcon="/icons/video-camera.svg"/>
            <TopIcon chatTopIcon="/icons/menu.svg"/>
        </div>
    </div>
    <div class="chat-window-wrap">

    </div>
    <div class="text-input-wrap">
        <input bind:value={texts}/>
        <div class="chatting-bottom-wrap">
            <div class="chatting-bottom-icon-wrap">
                <BottomIcon textBottomIcon="/icons/sidebar/face.svg"/>
                <BottomIcon textBottomIcon="/icons/calendar.svg"/>
                <BottomIcon textBottomIcon="/icons/file.svg"/>
            </div>
            <div class="message-go-wrap">
                <button class="message-go">전송</button>
            </div>
        </div>
    </div>
</div>

<style>
    .chatting-wrap {
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        background-color: #9bbbd4;
    }

    .chatting-top-wrap {
        width: 100%;
        height: 60px;
        display: flex;
        background-color: #9bbbd4;
    }

    .chatting-img-wrap {
        width: 60px;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    #chatting-img {
        width: 40px;
        height: 40px;
        border-radius: 15px;
    }

    .chatting-title-wrap {
        flex-grow: 1;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .chatting-title {
        font-weight: 500;
    }

    .chatting-icon-wrap {
        width: 130px;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .chat-window-wrap {
        width: 100%;
        flex-grow: 1;
    }

    .text-input-wrap {
        width: 100%;
        height: 110px;
    }

    .text-input-wrap input {
        border: none;
        width: 100%;
        height: 70px;
        padding: 0;
        display: flex;
    }

    .text-input-wrap input:focus {
        outline: none;
    }

    .chatting-bottom-wrap {
        background-color: white;
        width: 100%;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .chatting-bottom-icon-wrap {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100px;
        height: 100%;
    }

    .message-go-wrap {
        width: 80px;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .message-go {
        background-color: #fef01b;
        border: none;
        padding: 5px 13px;
        border-radius: 3px;
    }
</style>