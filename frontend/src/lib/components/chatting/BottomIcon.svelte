<script>
    export let textBottomIcon = ""
</script>

<button class="text-icon">
    <img src={textBottomIcon} alt="Icon" id="text-icon"/>
</button>

<style>
    .text-icon {
        width: 30px;
        height: 30px;
        display: flex;
        align-items: center;
        justify-content: center;
        border: none;
        background-color: transparent;
    }

    #text-icon {
        width: 20px;
    }
</style>