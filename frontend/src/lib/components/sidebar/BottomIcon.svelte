<script>
    export let bottomIconTitle = ""
    export let bottomIcon = ""
</script>

<div class="bottom-button-wrap">
    <button title={bottomIconTitle}>
        <img src={bottomIcon} alt="Icon" id="side-menu-icon"/>
    </button>
</div>

<style>
    .bottom-button-wrap {
        margin-top: 30px;
        width: 100%;
        height: 40px;
        margin: 0;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .bottom-button-wrap button {
        border-radius: 50%;
        background-color: transparent;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        width: 30px;
        height: 30px;
        padding: 0;
        border: 0;
        margin: 0;
    }

    #side-menu-icon {
        width: 18px;
    }
</style>