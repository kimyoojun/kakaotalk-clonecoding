<script>
    export let topIconTitle = ""
    export let topIcon = ""
    export let pageMove = ""

    const click = () => {
        window.location.href = pageMove
    }
</script>

<div class="top-button-wrap">
    <button title={topIconTitle} on:click={click}>
        <img src={topIcon} alt="Icon" id="side-menu-icon"/>
    </button>
</div>

<style>
    .top-button-wrap {
        margin-top: 30px;
        width: 100%;
        height: 55px;
        margin: 0;
    }

    .top-button-wrap button {
        background-color: transparent;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        width: 100%;
        height: 100%;
        padding: 0;
        border: 0;
        margin: 0;
    }

    .top-button-wrap img {
        width: 30px;
    }
</style>
