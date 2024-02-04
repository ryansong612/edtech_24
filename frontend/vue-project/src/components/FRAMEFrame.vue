<template>
  <main :class="$style.fRAMEFrame">
    <section :class="$style.fRAMEFrame1">
      <FRAMEFrame1 />
      <div :class="$style.magicWandComponentWrapper">
        <div :class="$style.magicWandComponent">
          <div :class="$style.magicBarParent">
            <img
              :class="$style.magicIcon"
              loading="eager"
              alt=""
              src="/magic.svg"
            />
          </div>
          <img
            :class="$style.historyQueryIcon"
            loading="eager"
            alt=""
            src="/historyquery.svg"
          />
        </div>
      </div>
    </section>
  </main>
</template>
<script>
  import { defineComponent } from "vue";
  import FRAMEFrame1 from "./FRAMEFrame1.vue";

  export default defineComponent({
    name: "FRAMEFrame",
    components: { FRAMEFrame1 },
  });
</script>
<style module>
  .magicIcon {
    width: 24px;
    height: 24px;
    position: relative;
  }
  .magicBarParent {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-10xs) 0px 0px;
  }
  .historyQueryIcon {
    height: 24px;
    width: 24px;
    position: relative;
  }
  .magicWandComponent {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-8xs);
  }
  .magicWandComponentWrapper {
    width: 721px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: center;
    padding: 0px var(--padding-xl);
    box-sizing: border-box;
    max-width: 100%;
  }
  .fRAMEFrame1 {
    align-self: stretch;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    justify-content: flex-start;
    gap: var(--gap-297xl);
    max-width: 100%;
    text-align: left;
    font-size: var(--font-size-17xl);
    color: var(--color-white);
    font-family: var(--font-inika);
  }
  .fRAMEFrame {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-71xl) 0px 0px;
    box-sizing: border-box;
    min-width: 951px;
    max-width: 100%;
  }

  @media screen and (max-width: 1200px) {
    .fRAMEFrame1 {
      gap: var(--gap-297xl);
    }
  }
  @media screen and (max-width: 1050px) {
    .fRAMEFrame {
      padding-top: var(--padding-39xl);
      box-sizing: border-box;
      min-width: 100%;
    }
  }
  @media screen and (max-width: 750px) {
    .fRAMEFrame1 {
      gap: var(--gap-297xl);
    }
  }
  @media screen and (max-width: 450px) {
    .fRAMEFrame1 {
      gap: var(--gap-297xl);
    }

    .fRAMEFrame {
      padding-top: var(--padding-19xl);
      box-sizing: border-box;
    }
  }
</style>
