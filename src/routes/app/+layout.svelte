<script>
    import NavBar from "$lib/components/sidebar/NavBar.svelte";
    import TopIcorn from "$lib/components/sidebar/TopIcorn.svelte";
    import BottomIcon from "$lib/components/sidebar/BottomIcon.svelte";
</script>

<div class="kakao-wrap">
    <NavBar>
        <div class="sidebar-icon-wrap">
            <TopIcorn topIcon="/icons/sidebar/profile.svg" topIconTitle="친구" pageMove="/app/friend"/>
            <TopIcorn topIcon="/icons/sidebar/chat.svg" topIconTitle="채팅"/>
            <TopIcorn topIcon="/icons/sidebar/more.svg" topIconTitle="더보기"/>
        </div>
        <div class="sidebar-icon-wrap">
            <BottomIcon bottomIcon="/icons/sidebar/face.svg" bottomIconTitle="카카오 이모티콘샵"/>
            <BottomIcon bottomIcon="/icons/sidebar/bell.svg" bottomIconTitle="알림"/>
            <BottomIcon bottomIcon="/icons/sidebar/settings.svg" bottomIconTitle="설정"/>
        </div>
    </NavBar>
    <slot/>
</div>

<style>
    .kakao-wrap {
        display: flex;
        width: 100%;
        height: 100%;
    }

    .sidebar-icon-wrap {
        margin: 30px 0;
    }
</style>
