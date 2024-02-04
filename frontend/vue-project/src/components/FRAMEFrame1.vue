<template>
  <div :class="$style.fRAMEFrame">
    <div :class="$style.fRAMEMyDatabase">
      <div :class="$style.tEXTsearchlargeenabled">
        <div :class="$style.iNSTANCEFieldcolor">
          <div :class="$style.tEXTplaceholdertext">
            <h1 :class="$style.myDatabase">My database</h1>
          </div>
          <div :class="$style.iNSTANCEbuttontertiarys">
            <div :class="$style.fRAMEButton">
              <div :class="$style.searchIconFrame">
                <div :class="$style.searchLarge01Enabled">
                  <div :class="$style.fieldColor" />
                  <div :class="$style.bottomBorder" />
                  <div :class="$style.spacer">
                    <div :class="$style.spacer1" />
                  </div>
                  <input
                    :class="$style.placeholderText"
                    placeholder="What are you looking for today?"
                    type="text"
                  />
                  <img
                    :class="$style.iconImageSearch16"
                    alt=""
                    src="/icon--image--search--16@2x.png"
                  />
                </div>
              </div>
              <div :class="$style.button03TertiarySmall">
                <img
                  :class="$style.backgroundIcon"
                  alt=""
                  src="/background.svg"
                />
                <div :class="$style.spacer2">
                  <div :class="$style.spacer3" />
                </div>
                <input :class="$style.label" placeholder="Filter" type="text" />
              </div>
            </div>
            <div :class="$style.button">
              <img
                :class="$style.backgroundIcon1"
                loading="eager"
                alt=""
                src="/background-1.svg"
              />
              <div :class="$style.spacer4">
                <div :class="$style.spacer5" />
              </div>
              <div :class="$style.label1">Create newquestion</div>
            </div>
          </div>
        </div>
        <img
          :class="$style.frameIcon"
          loading="eager"
          alt=""
          src="/vector-8.svg"
        />
      </div>
    </div>
    <div :class="$style.tagGrayEnabledFrame">
      <div :class="$style.tagDefaultGrayEnabledFrame">
        <div :class="$style.pleaseWriteQuestionsHereTe">
          <div :class="$style.tag01DefaultGray01E">
            <div :class="$style.tagColor" />
            <div :class="$style.labelText">Component</div>
            <div :class="$style.spacer6">
              <div :class="$style.spacer7" />
            </div>
          </div>
          <button :class="$style.tag01DefaultGray01E1">
            <div :class="$style.tagColor1" />
            <div :class="$style.labelTextWrapper">
              <div :class="$style.labelText1">New filtration</div>
            </div>
            <div :class="$style.spacer8">
              <div :class="$style.spacer9" />
            </div>
          </button>
        </div>
      </div>
      <div :class="$style.frameParent">
        <div :class="$style.frameWrapper">
          <div :class="$style.frameGroup">
            <div :class="$style.frameContainer">
              <div :class="$style.databaseFrameWrapper">
                <div :class="$style.databaseFrame">
                  <div :class="$style.pleaseWriteThe">
                    Please write the questions here
                  </div>
                  <img
                    :class="$style.magicIcon"
                    loading="eager"
                    alt=""
                    src="/magic.svg"
                  />
                </div>
              </div>
              <div :class="$style.frameChild" />
              <div :class="$style.frameItem" />
              <div :class="$style.frameDiv">
                <div :class="$style.dropdownMenuParent">
                  <div :class="$style.dropdownMenu">
                    <div :class="$style.dropdown01Default02Lab">
                      <img
                        :class="$style.fieldColorIcon"
                        alt=""
                        src="/field-color.svg"
                      />
                      <div :class="$style.labelText2">Type pf question</div>
                      <div :class="$style.dropdownChevron">
                        <div :class="$style.helperTextFrame">
                          <div :class="$style.inputText">Choose an option</div>
                          <img
                            :class="$style.iconNavigationChevron"
                            alt=""
                            src="/icon--navigation--chevron--down--16.svg"
                          />
                        </div>
                        <div :class="$style.dropdownFrame">
                          <div :class="$style.borderBottom" />
                          <div :class="$style.helperText" />
                        </div>
                      </div>
                    </div>
                  </div>
                  <img
                    :class="$style.deleteButtonIcon"
                    loading="eager"
                    alt=""
                    src="/vector-7.svg"
                  />
                </div>
              </div>
              <div :class="$style.codeSnippetMultiLineCl">
                <div :class="$style.background" />
                <div :class="$style.showMoreButton">
                  <div :class="$style.background1" />
                  <div :class="$style.spacer10">
                    <div :class="$style.spacer11" />
                  </div>
                  <div :class="$style.spacer12">
                    <div :class="$style.spacer13" />
                  </div>
                  <div :class="$style.label2">Show more</div>
                  <img
                    :class="$style.actionsNavigationChevron"
                    alt=""
                    src="/icon--navigation--chevron--down--16.svg"
                  />
                </div>
                <div :class="$style.codeWrapper">
                  <div :class="$style.code">
                    <p :class="$style.togglestateElement">
                      toggleState = (element, evt) =&gt; {
                    </p>
                    <p :class="$style.constData">
                      const data = element.dataset;
                    </p>
                    <p :class="$style.constLabel">
                      const label = (data.label) ?data.label : '';
                    </p>
                    <p :class="$style.constPreviousvalue">
                      const previousValue = (data.previousValue) ?
                    </p>
                    <p :class="$style.datapreviousvalue">
                      data.previousValue : '';
                    </p>
                    <p :class="$style.constInitialevt">
                      const initialEvt = evt;
                    </p>
                    <p :class="$style.thischangestate">this.changeState({</p>
                    <p :class="$style.groupDataevent">group: data.event,</p>
                    <p :class="$style.element">element,</p>
                    <p :class="$style.label3">label,</p>
                  </div>
                </div>
                <img
                  :class="$style.copyButtonIcon"
                  loading="eager"
                  alt=""
                  src="/copy-button@2x.png"
                />
              </div>
              <img :class="$style.deleteIcon" alt="" src="/delete.svg" />
            </div>
            <div :class="$style.modalPiecesButton01PWrapper">
              <div :class="$style.modalPiecesButton01P">
                <img
                  :class="$style.backgroundIcon2"
                  alt=""
                  src="/background-2.svg"
                />
                <div :class="$style.spacer14">
                  <div :class="$style.spacer15" />
                </div>
                <input :class="$style.label4" placeholder="Save" type="text" />
              </div>
            </div>
          </div>
        </div>
        <div :class="$style.modalPrimaryButton" />
      </div>
    </div>
  </div>
</template>
<script>
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "FRAMEFrame1",
  });
</script>
<style module>
  .myDatabase {
    margin: 0;
    height: 58px;
    position: relative;
    font-size: inherit;
    line-height: 150%;
    font-weight: 400;
    font-family: inherit;
    display: inline-block;
    flex-shrink: 0;
  }
  .tEXTplaceholdertext {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px 0px var(--padding-9xs);
  }
  .fieldColor {
    position: absolute;
    width: 100%;
    top: 0px;
    right: 0px;
    left: 0px;
    background-color: var(--color-gray-200);
    border-bottom: 1px solid var(--color-dimgray-100);
    box-sizing: border-box;
    height: 48.5px;
  }
  .bottomBorder {
    position: absolute;
    top: 47px;
    left: 0px;
    background-color: var(--color-dimgray-100);
    width: 512px;
    height: 1px;
    display: none;
  }
  .spacer1 {
    position: absolute;
    width: 100%;
    top: 0px;
    right: 0px;
    left: 0px;
    height: 100%;
    display: none;
  }
  .spacer {
    position: absolute;
    top: 0px;
    right: 0px;
    width: 48px;
    height: 48px;
    display: none;
  }
  .placeholderText {
    border: none;
    outline: none;
    font-family: var(--font-ibm-plex-sans);
    font-size: var(--font-size-sm);
    background-color: transparent;
    position: absolute;
    width: calc(100% - 96px);
    top: 15px;
    left: 48px;
    letter-spacing: 0.16px;
    line-height: 18px;
    color: var(--color-dimgray-100);
    text-align: left;
    display: inline-block;
    z-index: 1;
  }
  .iconImageSearch16 {
    position: absolute;
    top: 16px;
    left: 16px;
    width: 16px;
    height: 16px;
    object-fit: cover;
    z-index: 1;
  }
  .searchLarge01Enabled {
    align-self: stretch;
    height: 55.6px;
    position: relative;
  }
  .searchIconFrame {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px 0px var(--padding-mid);
    box-sizing: border-box;
    min-width: 333px;
    max-width: 100%;
  }
  .backgroundIcon {
    height: 100%;
    width: 100%;
    position: absolute;
    margin: 0 !important;
    top: 0.4px;
    right: 0px;
    bottom: -0.4px;
    left: 0px;
    max-width: 100%;
    overflow: hidden;
    max-height: 100%;
  }
  .spacer3 {
    position: absolute;
    top: 0px;
    right: 0px;
    width: 64px;
    height: 128px;
    display: none;
  }
  .spacer2 {
    height: 32px;
    width: 64px;
    position: relative;
    display: none;
    z-index: 1;
  }
  .label {
    width: 32px;
    border: none;
    outline: none;
    font-family: var(--font-ibm-plex-sans);
    font-size: var(--font-size-sm);
    background-color: transparent;
    height: 18px;
    position: relative;
    letter-spacing: 0.16px;
    line-height: 18px;
    color: var(--color-white);
    text-align: left;
    display: inline-block;
    z-index: 1;
  }
  .button03TertiarySmall {
    width: 124px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    padding: var(--padding-6xs) var(--padding-base);
    box-sizing: border-box;
    position: relative;
  }
  .fRAMEButton {
    flex: 1;
    display: flex;
    flex-direction: row;
    align-items: flex-end;
    justify-content: flex-start;
    gap: var(--gap-17xl);
    min-width: 437px;
    max-width: 100%;
  }
  .backgroundIcon1 {
    height: 48px;
    width: 100%;
    position: absolute;
    margin: 0 !important;
    right: 0px;
    bottom: -13px;
    left: 0px;
    max-width: 100%;
    overflow: hidden;
  }
  .spacer5 {
    position: absolute;
    top: 0px;
    right: 0px;
    width: 64px;
    height: 128px;
    display: none;
  }
  .spacer4 {
    height: 48px;
    width: 64px;
    position: absolute;
    margin: 0 !important;
    right: 0px;
    bottom: -13px;
    z-index: 1;
  }
  .label1 {
    position: relative;
    letter-spacing: 0.16px;
    line-height: 18px;
    z-index: 2;
  }
  .button {
    height: 35px;
    display: flex;
    flex-direction: row;
    align-items: flex-end;
    justify-content: flex-start;
    padding: var(--padding-mini) var(--padding-11xl) var(--padding-12xs)
      var(--padding-base);
    box-sizing: border-box;
    position: relative;
  }
  .iNSTANCEbuttontertiarys {
    width: 910px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-41xl);
    max-width: 100%;
    font-size: var(--font-size-sm);
    font-family: var(--font-ibm-plex-sans);
  }
  .iNSTANCEFieldcolor {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    gap: var(--gap-xl);
    max-width: 100%;
  }
  .frameIcon {
    align-self: stretch;
    position: relative;
    max-width: 100%;
    overflow: hidden;
    max-height: 100%;
  }
  .tEXTsearchlargeenabled {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    justify-content: flex-start;
    padding: 0px 0px 0px var(--padding-8xs);
    box-sizing: border-box;
    gap: var(--gap-4xl);
    max-width: 100%;
  }
  .fRAMEMyDatabase {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px var(--padding-5xs);
    box-sizing: border-box;
    max-width: 100%;
  }
  .tagColor {
    height: 100%;
    width: 100%;
    position: absolute;
    margin: 0 !important;
    top: 0.4px;
    right: 0px;
    bottom: -0.4px;
    left: 0px;
    border-radius: var(--br-lg);
    background-color: var(--color-darkslategray-100);
  }
  .labelText {
    position: relative;
    letter-spacing: 0.32px;
    line-height: 16px;
    z-index: 1;
  }
  .spacer7 {
    position: absolute;
    top: 0px;
    right: 0px;
    width: 8px;
    height: 16px;
  }
  .spacer6 {
    height: 24px;
    width: 8px;
    position: relative;
    z-index: 1;
  }
  .tag01DefaultGray01E {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    padding: 0px 0px 0px var(--padding-5xs);
    position: relative;
    gap: var(--gap-11xs);
  }
  .tagColor1 {
    height: 100%;
    width: 100%;
    position: absolute;
    margin: 0 !important;
    top: 0px;
    right: 0px;
    bottom: 0px;
    left: 0px;
    border-radius: var(--br-lg);
    background-color: var(--color-darkslategray-100);
  }
  .labelText1 {
    position: relative;
    font-size: var(--font-size-xs);
    letter-spacing: 0.32px;
    line-height: 16px;
    font-family: var(--font-ibm-plex-sans);
    color: var(--color-whitesmoke);
    text-align: left;
    z-index: 1;
  }
  .labelTextWrapper {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px 0px 0px 0px;
  }
  .spacer9 {
    position: absolute;
    top: 0px;
    right: 0px;
    width: 8px;
    height: 16px;
  }
  .spacer8 {
    height: 24px;
    width: 8px;
    position: relative;
    z-index: 1;
  }
  .tag01DefaultGray01E1 {
    cursor: pointer;
    border: none;
    padding: 0px 0px 0px var(--padding-5xs);
    background-color: transparent;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    position: relative;
  }
  .pleaseWriteQuestionsHereTe {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-5xl);
  }
  .tagDefaultGrayEnabledFrame {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px var(--padding-xs);
  }
  .pleaseWriteThe {
    position: relative;
    line-height: 24px;
    z-index: 1;
  }
  .magicIcon {
    width: 24px;
    height: 24px;
    position: relative;
    z-index: 3;
  }
  .databaseFrame {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-75xl);
  }
  .databaseFrameWrapper {
    width: 388px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-lg) 0px 0px;
    box-sizing: border-box;
    max-width: 100%;
  }
  .frameChild {
    height: calc(100% - 2px);
    width: 755px;
    position: absolute;
    margin: 0 !important;
    top: 2px;
    bottom: 0px;
    left: 1px;
    background-color: var(--color-gray-200);
  }
  .frameItem {
    align-self: stretch;
    width: 1423px;
    position: relative;
    border: 1px solid var(--color-cornflowerblue);
    box-sizing: border-box;
    display: none;
    max-width: 100%;
    z-index: 2;
  }
  .fieldColorIcon {
    width: 100%;
    height: 40px;
    position: absolute;
    margin: 0 !important;
    right: 0px;
    bottom: 20px;
    left: 0px;
    max-width: 100%;
    overflow: hidden;
    flex-shrink: 0;
  }
  .labelText2 {
    align-self: stretch;
    position: relative;
    letter-spacing: 0.32px;
    line-height: 16px;
  }
  .inputText {
    flex: 1;
    position: relative;
    letter-spacing: 0.16px;
    line-height: 18px;
    z-index: 1;
  }
  .iconNavigationChevron {
    height: 16px;
    width: 16px;
    position: relative;
    z-index: 1;
  }
  .helperTextFrame {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    padding: 0px var(--padding-base);
    gap: var(--gap-base);
  }
  .borderBottom {
    align-self: stretch;
    height: 1px;
    position: relative;
    background-color: var(--color-dimgray-100);
    z-index: 1;
  }
  .helperText {
    align-self: stretch;
    flex: 1;
    position: relative;
    letter-spacing: 0.32px;
    line-height: 16px;
  }
  .dropdownFrame {
    align-self: stretch;
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-7xs);
    font-size: var(--font-size-xs);
    color: var(--color-gray-100);
  }
  .dropdownChevron {
    align-self: stretch;
    height: 51px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    gap: var(--gap-3xs);
    font-size: var(--font-size-sm);
    color: var(--color-whitesmoke);
  }
  .dropdown01Default02Lab {
    align-self: stretch;
    height: 82px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px 0px 0px;
    box-sizing: border-box;
    position: relative;
    gap: var(--gap-mid);
    z-index: 3;
  }
  .dropdownMenu {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px 0px var(--padding-3xs);
  }
  .deleteButtonIcon {
    height: 149px;
    width: 1px;
    position: relative;
    z-index: 1;
  }
  .dropdownMenuParent {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: flex-end;
    justify-content: flex-start;
    gap: var(--gap-27xl);
  }
  .frameDiv {
    width: 302px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px 0px var(--padding-10xs);
    box-sizing: border-box;
    font-size: var(--font-size-xs);
    color: var(--color-silver);
  }
  .background {
    height: 100%;
    width: 100%;
    position: absolute;
    margin: 0 !important;
    top: 0px;
    right: 0px;
    bottom: 0px;
    left: 0px;
    background-color: var(--color-gray-200);
  }
  .background1 {
    position: absolute;
    width: 100%;
    top: 0px;
    right: 0px;
    left: 0px;
    height: 100%;
  }
  .spacer11 {
    position: absolute;
    top: 0px;
    right: 0px;
    width: 100%;
    height: 100%;
  }
  .spacer10 {
    position: absolute;
    top: 0px;
    right: 0px;
    width: 16px;
    height: 32px;
  }
  .spacer13 {
    position: absolute;
    top: 0px;
    right: 0px;
    width: 8px;
    height: 16px;
  }
  .spacer12 {
    position: absolute;
    top: 0px;
    right: 32px;
    width: 8px;
    height: 32px;
  }
  .label2 {
    position: absolute;
    top: 7px;
    left: 16px;
    letter-spacing: 0.16px;
    line-height: 18px;
  }
  .actionsNavigationChevron {
    position: absolute;
    top: 8px;
    right: 16px;
    width: 16px;
    height: 16px;
  }
  .showMoreButton {
    height: 32px;
    width: 129px;
    position: relative;
    display: none;
    z-index: 1;
  }
  .togglestateElement {
    margin: 0;
  }
  .constData {
    margin: 0;
  }
  .constLabel {
    margin: 0;
  }
  .constPreviousvalue {
    margin: 0;
  }
  .datapreviousvalue {
    margin: 0;
  }
  .constInitialevt {
    margin: 0;
  }
  .thischangestate {
    margin: 0;
  }
  .groupDataevent {
    margin: 0;
  }
  .element {
    margin: 0;
  }
  .label3 {
    margin: 0;
  }
  .code {
    align-self: stretch;
    position: relative;
    letter-spacing: 0.32px;
    line-height: 16px;
    white-space: pre-wrap;
    z-index: 1;
  }
  .codeWrapper {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-5xs) 0px 0px;
    box-sizing: border-box;
    min-width: 385px;
    max-width: 100%;
    font-size: var(--font-size-xs);
    color: var(--color-whitesmoke);
    font-family: var(--font-ibm-plex-mono);
  }
  .copyButtonIcon {
    height: 32px;
    width: 32px;
    position: relative;
    object-fit: contain;
    z-index: 1;
  }
  .codeSnippetMultiLineCl {
    flex: 1;
    overflow: hidden;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-5xs) var(--padding-5xs) var(--padding-base)
      var(--padding-base);
    box-sizing: border-box;
    position: relative;
    gap: var(--gap-base);
    min-width: 432px;
    max-width: 100%;
    font-size: var(--font-size-sm);
    color: var(--color-cornflowerblue);
  }
  .deleteIcon {
    height: 12.3px;
    width: 17px;
    position: absolute;
    margin: 0 !important;
    right: 26px;
    bottom: 89.4px;
    z-index: 4;
  }
  .frameContainer {
    align-self: stretch;
    border: 1px solid var(--color-cornflowerblue);
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    padding: 0px var(--padding-9xs) var(--padding-11xs) var(--padding-2xl);
    position: relative;
    gap: var(--gap-3xl);
    max-width: 100%;
    z-index: 2;
  }
  .backgroundIcon2 {
    height: 64px;
    width: 100%;
    position: absolute;
    margin: 0 !important;
    right: 0px;
    bottom: -20.6px;
    left: 0px;
    max-width: 100%;
    overflow: hidden;
  }
  .spacer15 {
    position: absolute;
    top: 0px;
    right: -0.2px;
    width: 64px;
    height: 128px;
    display: none;
  }
  .spacer14 {
    height: 43.4px;
    width: 82.8px;
    position: relative;
    display: none;
    z-index: 1;
  }
  .label4 {
    width: 29px;
    border: none;
    outline: none;
    font-family: var(--font-ibm-plex-sans);
    font-size: var(--font-size-sm);
    background-color: transparent;
    height: 18px;
    position: relative;
    letter-spacing: 0.16px;
    line-height: 18px;
    color: var(--color-white);
    text-align: left;
    display: inline-block;
    z-index: 1;
  }
  .modalPiecesButton01P {
    flex: 1;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    padding: var(--padding-mini) var(--padding-base) var(--padding-3xs);
    box-sizing: border-box;
    position: relative;
    max-width: 100%;
  }
  .modalPiecesButton01PWrapper {
    width: 381px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px var(--padding-11xl) 0px var(--padding-xl);
    box-sizing: border-box;
    max-width: 100%;
  }
  .frameGroup {
    align-self: stretch;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    gap: var(--gap-43xl);
    max-width: 100%;
  }
  .frameWrapper {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px 0px var(--padding-6xs);
    box-sizing: border-box;
    min-width: 925px;
    max-width: 100%;
  }
  .modalPrimaryButton {
    height: 290px;
    width: 11px;
    position: relative;
    border-radius: var(--br-xl);
    background-color: var(--color-gainsboro);
  }
  .frameParent {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: flex-end;
    justify-content: flex-start;
    gap: var(--gap-10xl);
    max-width: 100%;
    font-size: var(--font-size-base);
    color: var(--color-dimgray-200);
  }
  .tagGrayEnabledFrame {
    align-self: stretch;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-7xl);
    max-width: 100%;
    font-size: var(--font-size-xs);
    color: var(--color-whitesmoke);
    font-family: var(--font-ibm-plex-sans);
  }
  .fRAMEFrame {
    align-self: stretch;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-smi);
    max-width: 100%;
    text-align: left;
    font-size: var(--font-size-17xl);
    color: var(--color-white);
    font-family: var(--font-inika);
  }

  @media screen and (max-width: 1200px) {
    .iNSTANCEFieldcolor {
      flex-wrap: wrap;
    }

    .frameContainer {
      flex-wrap: wrap;
    }

    .modalPrimaryButton {
      width: 100%;
      height: 11px;
    }

    .frameParent {
      flex-wrap: wrap;
    }
  }
  @media screen and (max-width: 1050px) {
    .myDatabase {
      font-size: var(--font-size-10xl);
      line-height: 43px;
    }

    .iNSTANCEbuttontertiarys {
      flex-wrap: wrap;
      gap: var(--gap-41xl);
    }

    .frameWrapper {
      min-width: 100%;
    }
  }
  @media screen and (max-width: 750px) {
    .fRAMEButton {
      flex-wrap: wrap;
      gap: var(--gap-17xl);
      min-width: 100%;
    }

    .codeWrapper {
      min-width: 100%;
    }

    .codeSnippetMultiLineCl {
      flex-wrap: wrap;
      min-width: 100%;
    }

    .frameGroup {
      gap: var(--gap-43xl);
    }
  }
  @media screen and (max-width: 450px) {
    .myDatabase {
      font-size: var(--font-size-3xl);
      line-height: 32px;
    }

    .dropdownMenuParent {
      gap: var(--gap-27xl);
    }

    .frameGroup {
      gap: var(--gap-43xl);
    }
  }
</style>
