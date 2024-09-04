<script setup lang="ts">
import { LockOutlined, MobileOutlined, UserOutlined } from '@ant-design/icons-vue'
import { delayTimer } from '@v-c/utils'
import { AxiosError } from 'axios'
import GlobalLayoutFooter from '~/layouts/components/global-footer/index.vue'
import { registerApi } from '~/api/auth/register'
import { getQueryParam } from '~/utils/tools'
import type { RegisterMobileParams, RegisterParams } from '~@/api/auth/register'
import pageBubble from '@/utils/page-bubble'

const message = useMessage()
const notification = useNotification()
const appStore = useAppStore()
const { layoutSetting } = storeToRefs(appStore)
const router = useRouter()
const token = useAuthorization()
const registerModel = reactive({
  username: undefined,
  password: undefined,
  mobile: undefined,
  code: undefined,
  type: 'account',
  remember: true,
})
const { t } = useI18nLocale()
const formRef = shallowRef()
const codeLoading = shallowRef(false)
const resetCounter = 60
const submitLoading = shallowRef(false)
const errorAlert = shallowRef(false)
const bubbleCanvas = ref<HTMLCanvasElement>()
const { counter, pause, reset, resume, isActive } = useInterval(1000, {
  controls: true,
  immediate: false,
  callback(count) {
    if (count) {
      if (count === resetCounter)
        pause()
    }
  },
})
async function getCode() {
  codeLoading.value = true
  try {
    await formRef.value.validate(['mobile'])
    setTimeout(() => {
      reset()
      resume()
      codeLoading.value = false
      message.success('验证码是：123456')
    }, 3000)
  }
  catch (error) {
    codeLoading.value = false
  }
}
async function submit() {
  submitLoading.value = true
  try {
    await formRef.value?.validate()
    let params: RegisterParams | RegisterMobileParams

    if (registerModel.type === 'account') {
      params = {
        username: registerModel.username,
        password: registerModel.password,
      } as unknown as RegisterParams
    }
    else {
      params = {
        mobile: registerModel.mobile,
        code: registerModel.code,
        type: 'mobile',
      } as unknown as RegisterMobileParams
    }
    const { data } = await registerApi(params)
    token.value = data?.token
    notification.success({
      message: '注册成功',
      description: '欢迎回来！',
      duration: 3,
    })
    // 获取当前是否存在重定向的链接，如果存在就走重定向的地址
    const redirect = getQueryParam('redirect', '/')
    router.push({
      path: redirect,
      replace: true,
    })
  }
  catch (e) {
    if (e instanceof AxiosError) {
      errorAlert.value = true
    }
    submitLoading.value = false
  }
}
onMounted(async () => {
  await delayTimer(300)
  pageBubble.init(unref(bubbleCanvas)!)
})
onBeforeUnmount(() => {
  pageBubble.removeListeners()
})
</script>

<template>
  <div class="register-container">
    <div h-screen w-screen absolute z-10>
      <canvas ref="bubbleCanvas" />
    </div>
    <div class="register-content flex-center">
      <div class="nuii-form-register-main rounded">
        <!-- 登录头部 -->
        <div class="flex-between h-15 px-4 mb-[2px]">
          <div class="flex-end">
            <!-- <span class="nuii-form-register-logo"> -->
            <!-- <img w-full h-full object-cover src="/logo.svg" alt="" /> -->
            <!-- </span> -->
            <span class="nuii-form-register-title">
              Nuii
            </span>
            <span class="nuii-form-register-desc">
              {{ t("pages.layouts.userLayout.title") }}
            </span>
          </div>
          <div class="register-lang flex-center relative z-11">
            <span
              class="flex-center cursor-pointer text-16px"
              @click="appStore.toggleTheme(layoutSetting.theme === 'dark' ? 'light' : 'dark')">
              <!-- 亮色和暗黑模式切换按钮 -->
              <template v-if="layoutSetting.theme === 'light'">
                <carbon-moon />
              </template>
              <template v-else>
                <carbon-sun />
              </template>
            </span>
            <SelectLang />
          </div>
        </div>
        <a-divider m-0 />
        <!-- 登录主体 -->
        <div class="box-border flex min-h-[520px]">
          <!-- 登录框左侧 -->
          <div class="nuii-form-register-main-left min-h-[520px] flex-center  bg-[var(--bg-color-container)]">
            <!-- <img src="@/assets/images/login-left.png" class="h-5/6 w-5/6" alt="" /> -->
          </div>
          <a-divider m-0 type="vertical" class="nuii-register-divider  min-h-[520px]" />
          <!-- 登录框右侧 -->
          <div class="nuii-form-register-main-right px-5 w-[335px] flex-center flex-col relative z-11">
            <div class="text-center py-6 text-2xl">
              {{ t('pages.register.tips') }}
            </div>
            <a-form ref="formRef" :model="registerModel">
              <a-tabs v-model:activeKey="registerModel.type" centered>
                <a-tab-pane key="account" :tab="t('pages.register.accountRegister.tab')" />
                <a-tab-pane key="mobile" :tab="t('pages.register.phoneRegister.tab')" />
              </a-tabs>
              <!-- 判断是否存在error -->
              <a-alert
                v-if="errorAlert && registerModel.type === 'account'" mb-24px
                :message="t('pages.register.accountRegister.errorMessage')" type="error" show-icon
              />
              <a-alert
                v-if="errorAlert && registerModel.type === 'mobile'" mb-24px
                :message="t('pages.register.phoneRegister.errorMessage')" type="error" show-icon
              />
              <template v-if="registerModel.type === 'account'">
                <a-form-item name="username" :rules="[{ required: true, message: t('pages.register.username.required') }]">
                  <a-input
                    v-model:value="registerModel.username" allow-clear
                    autocomplete="off"
                    :placeholder="t('pages.register.username.placeholder')" size="large" @press-enter="submit"
                  >
                    <template #prefix>
                      <UserOutlined />
                    </template>
                  </a-input>
                </a-form-item>
                <a-form-item name="password" :rules="[{ required: true, message: t('pages.register.password.required') }]">
                  <a-input-password
                    v-model:value="registerModel.password" allow-clear
                    :placeholder="t('pages.register.password.placeholder')" size="large" @press-enter="submit"
                  >
                    <template #prefix>
                      <LockOutlined />
                    </template>
                  </a-input-password>
                </a-form-item>
              </template>
              <template v-if="registerModel.type === 'mobile'">
                <a-form-item
                  name="mobile" :rules="[
                    { required: true, message: t('pages.register.phoneNumber.required') },
                    {
                      pattern: /^(86)?1([38][0-9]|4[579]|5[0-35-9]|6[6]|7[0135678]|9[89])[0-9]{8}$/,
                      message: t('pages.register.phoneNumber.invalid'),
                    },
                  ]"
                >
                  <a-input
                    v-model:value="registerModel.mobile" allow-clear
                    :placeholder="t('pages.register.phoneNumber.placeholder')" size="large" @press-enter="submit"
                  >
                    <template #prefix>
                      <MobileOutlined />
                    </template>
                  </a-input>
                </a-form-item>
                <a-form-item name="code" :rules="[{ required: true, message: t('pages.register.captcha.required') }]">
                  <div flex items-center>
                    <a-input
                      v-model:value="registerModel.code"
                      style="flex: 1 1 0%; transition: width 0.3s ease 0s; margin-right: 8px;" allow-clear
                      :placeholder="t('pages.register.captcha.placeholder')" size="large" @press-enter="submit"
                    >
                      <template #prefix>
                        <LockOutlined />
                      </template>
                    </a-input>
                    <a-button :loading="codeLoading" :disabled="isActive" size="large" @click="getCode">
                      <template v-if="!isActive">
                        {{ t('pages.register.phoneRegister.getVerificationCode') }}
                      </template>
                      <template v-else>
                        {{ resetCounter - counter }} {{ t('pages.getCaptchaSecondText') }}
                      </template>
                    </a-button>
                  </div>
                </a-form-item>
              </template>
              <div class="mb-24px flex-between">
                <RouterLink to="/login">已经有账号？点击这里登录</RouterLink>
              </div>
              <a-button type="primary" block :loading="submitLoading" size="large" @click="submit">
                {{ t('pages.register.submit') }}
              </a-button>
            </a-form>
          </div>
        </div>
      </div>
    </div>
    <div py-24px px-50px fixed bottom-0 z-11 w-screen :data-theme="layoutSetting.theme" text-14px>
      <GlobalLayoutFooter :copyright="layoutSetting.copyright" icp="">
        <template #renderFooterLinks>
          <footer-links />
        </template>
      </GlobalLayoutFooter>
    </div>
  </div>
</template>

<style lang="less" scoped>
.register-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  overflow: auto;
  background: var(--bg-color-container);
}

.register-lang {
  height: 40px;
  line-height: 44px;
}

.register-content {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.nuii-form-register-container {
  display: flex;
  flex: 1 1;
  flex-direction: column;
  height: 100%;
  padding: 32px 0;
  overflow: auto;
  background: inherit
}

.nuii-form-register-header a {
  text-decoration: none
}

.nuii-form-register-title {
  color: var(--text-color);
  font-weight: 600;
  font-size: 33px;
  line-height: 1;
}

.nuii-form-register-logo {
  width: 44px;
  height: 44px;
  margin-right: 16px;
  vertical-align: top
}

.nuii-form-register-desc {
  color: var(--text-color-1);
  font-size: 14px;
  margin-left: 16px
}

.nuii-form-register-main-right {
  .ant-tabs-nav-list {
    margin: 0 auto;
    font-size: 16px;
  }

  .nuii-form-register-other {
    line-height: 22px;
    text-align: center
  }

}

.nuii-form-register-main {
  box-shadow: var(--c-shadow);
}

.icon {
  margin-left: 8px;
  color: var(--text-color-2);
  font-size: 24px;
  vertical-align: middle;
  cursor: pointer;
  transition: color .3s;

  &:hover {
    color: var(--pro-ant-color-primary);
  }
}

.register-media(@width:100%) {
  .nuii-form-register-main {
    width: @width;
  }
  .nuii-form-register-main-left {
    display: none;
  }
  .nuii-form-register-main-right {
    width: 100%;
  }
  .nuii-form-register-desc {
    display: none;
  }
}

@media (min-width : 992px) {
  .nuii-form-register-main-left{
    width: 700px;
  }
}

@media(min-width:768px) and (max-width:991px) {
  .nuii-register-divider {
    display: none;
  }
  .register-media(400px)
}

@media screen and (max-width:767px) {
  .register-media(350px);

  .nuii-register-divider {
    display: none;
  }
}
</style>
