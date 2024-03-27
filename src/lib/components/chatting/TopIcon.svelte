<script>
    export let chatTopIcon = ""
</script>

<button class="chat-top-icon">
    <img src={chatTopIcon} alt="Icon" id="chatting-icon"/>
</button>

<style>
    .chat-top-icon {
        display: flex;
        align-items: center;
        justify-content: center;
        border: none;
        width: 30px;
        height: 30px;
        border-radius: 50%;
        background-color: transparent;
    }

    #chatting-icon {
        width: 20px;
    }
</style>