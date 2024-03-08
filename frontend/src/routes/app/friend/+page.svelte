<script>
    import Profile from "$lib/components/profile.svelte";
</script>

<div class="friend-top-wrap">
    <div class="friend-top-element">
        <h2 class="friend-title">친구</h2>
    </div>
    <div class="friend-top-element">
        <div class="friend-icon-wrap">
            <img src="/icons/searched.svg" alt="Icon" title="통합검색" id="friend-top-icon"/>
        </div>
        <div class="friend-icon-wrap">
            <img src="/icons/plus-circle.svg" alt="Icon" title="친구 추가" id="friend-top-icon"/>
        </div>
    </div>
</div>

<Profile/>

<style>
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
    }

    #friend-top-icon {
        width: 25px;
    }

    .friend-title {
        margin: 0;
    }
</style>