import type { STATUS } from '~@/utils/constant'

interface UserTableModel {
  id: number
  parent_id: number
  department_id: number
  nickname: string
  username: string
  email: string
  password: string
  login_time: string
  login_status: number
  avatar: string
  status: number
  updated_by: number
  updated_time: string
  created_by: number
  created_time: string
  roles?: (string | number)[]
  pageSize?: number
}

type UserTableParams = Partial<Omit<UserTableModel, 'id'>>

export async function getListApi(params?: UserTableParams) {
  return useGet<UserTableModel[]>('/user/list', params)
}

export async function upsertApi(params: UserTableParams) {
  return usePost('/user/upsert', params)
}

export type {
  UserTableParams,
  UserTableModel,
}
