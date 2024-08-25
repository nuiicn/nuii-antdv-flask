export interface RegisterParams {
  username: string
  password: string
  type?: 'account'
}

export interface RegisterMobileParams {
  mobile: string
  code: string
  type: 'mobile'
}

export interface RegisterResultModel {
  token: string
}

export function registerApi(params: RegisterParams | RegisterMobileParams) {
  return usePost<RegisterResultModel, RegisterParams | RegisterMobileParams>('/auth/register', params, {
    // 设置为false的时候不会携带token
    token: false,
    // 开发模式下使用自定义的接口
    customDev: true,
    // 是否开启全局请求loading
    loading: true,
  })
}
