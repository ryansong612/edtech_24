<template>
  <div :class="$style.component7">
    <div :class="$style.fRAMEFRAME" />
    <div :class="$style.component4">
      <div :class="$style.rECTANGLERectangle" />
      <div :class="$style.component1">
        <div :class="$style.fRAMEFrame">
          <h1 :class="$style.home">Home</h1>
        </div>
        <div :class="$style.setting">Setting</div>
        <h1 :class="$style.myClass">My class</h1>
      </div>
    </div>
    <h1 :class="$style.myDatabass">My databass</h1>
  </div>
</template>
<script>
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "Component",
  });
</script>
<style module>
  .fRAMEFRAME {
    width: 100%;
    height: 100%;
    position: absolute;
    margin: 0 !important;
    top: 0px;
    right: 0px;
    bottom: 0px;
    left: 0px;
    background-color: var(--color-dimgray-400);
  }
  .rECTANGLERectangle {
    width: 132px;
    height: 132px;
    position: relative;
    border-radius: 50%;
    background-color: var(--color-dimgray-300);
  }
  .home {
    margin: 0;
    height: 113px;
    width: 285px;
    position: relative;
    font-size: inherit;
    line-height: 150%;
    font-weight: 400;
    font-family: inherit;
    display: inline-block;
    flex-shrink: 0;
  }
  .fRAMEFrame {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px 0px 0px 0px;
  }
  .setting {
    width: 122.6px;
    position: relative;
    line-height: 150%;
    color: var(--color-white);
    display: none;
    height: 93px;
    flex-shrink: 0;
  }
  .myClass {
    margin: 0;
    height: 50px;
    position: relative;
    font-size: inherit;
    line-height: 150%;
    font-weight: 400;
    font-family: inherit;
    display: inline-block;
    flex-shrink: 0;
  }
  .component1 {
    align-self: stretch;
    height: 283px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px var(--padding-13xl) var(--padding-101xl) 0px;
    box-sizing: border-box;
  }
  .component4 {
    align-self: stretch;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-184xl) 0px var(--padding-185xl);
    gap: var(--gap-150xl);
    z-index: 1;
  }
  .myDatabass {
    margin: 0 !important;
    height: 57.8px;
    position: absolute;
    bottom: 365.1px;
    left: 73px;
    font-size: inherit;
    line-height: 150%;
    font-weight: 400;
    font-family: inherit;
    color: var(--color-white);
    display: inline-block;
    z-index: 2;
  }
  .component7 {
    height: 1280px;
    width: 396px;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    justify-content: center;
    padding: var(--padding-115xl) var(--padding-18xl) var(--padding-115xl)
      var(--padding-55xl);
    box-sizing: border-box;
    position: relative;
    max-width: 100%;
    text-align: left;
    font-size: var(--font-size-17xl);
    color: var(--color-dimgray-300);
    font-family: var(--font-inika);
  }

  @media screen and (max-width: 1200px) {
    .component7 {
      padding-top: var(--padding-68xl);
      padding-bottom: var(--padding-68xl);
      box-sizing: border-box;
    }
  }
  @media screen and (max-width: 1050px) {
    .home {
      font-size: var(--font-size-10xl);
      line-height: 43px;
    }

    .setting {
      font-size: var(--font-size-10xl);
      line-height: 43px;
    }

    .myClass {
      font-size: var(--font-size-10xl);
      line-height: 43px;
    }

    .component4 {
      padding-top: var(--padding-113xl);
      padding-bottom: var(--padding-114xl);
      box-sizing: border-box;
    }

    .myDatabass {
      font-size: var(--font-size-10xl);
      line-height: 43px;
    }
  }
  @media screen and (max-width: 750px) {
    .component4 {
      padding-top: var(--padding-67xl);
      padding-bottom: var(--padding-67xl);
      box-sizing: border-box;
    }

    .component7 {
      padding-top: var(--padding-38xl);
      padding-bottom: var(--padding-38xl);
      box-sizing: border-box;
    }
  }
  @media screen and (max-width: 450px) {
    .home {
      font-size: var(--font-size-3xl);
      line-height: 32px;
    }

    .setting {
      font-size: var(--font-size-3xl);
      line-height: 32px;
    }

    .myClass {
      font-size: var(--font-size-3xl);
      line-height: 32px;
    }

    .component4 {
      gap: var(--gap-150xl);
    }

    .myDatabass {
      font-size: var(--font-size-3xl);
      line-height: 32px;
    }

    .component7 {
      padding-left: var(--padding-xl);
      box-sizing: border-box;
    }
  }
</style>
