<script>
  import Sidebar from "$lib/Sidebar.svelte";
</script>

<body>
  <div class="bst">
    <!-- Level 1 -->
    <div class="node level-1">I</div>

    <!-- Level 2 -->
    <div class="node level-2 left">1A</div>
    <div class="node level-2 right">1D</div>

    <!-- Level 3 -->
    <div class="node level-3 left">2A</div>
    <div class="node level-3 right">2D</div>
  </div>
</body>

<Sidebar />

<style>
  body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
  }

  .bst {
    position: relative;
  }

  .node {
    width: 40px;
    height: 40px;
    background-color: #3498db;
    color: #fff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    position: absolute;
  }

  .line {
    position: absolute;
    border: 2px solid #3498db;
    border-radius: 4px;
    width: 0;
  }

  .level-1 {
    top: 10px;
  }

  .level-2 {
    top: 60px;
  }

  .level-3 {
    top: 110px;
  }

  .left {
    left: 50%;
    transform: translateX(-100%);
  }

  .right {
    left: 50%;
    transform: translateX(50%);
  }
</style>
