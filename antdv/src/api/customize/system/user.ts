interface UserTableModel {
  id: string
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
  roles: (string | number)[]
  current: number
  pageSize: number
  column?: string
  value?: string
}

interface UserTableColumn {
  dataIndex: keyof UserTableModel
}

interface UpdateTableColumn {
  id: string
  column: string
  value: string
}

type UserTableParams = Partial<Omit<UserTableModel, 'id'>>

export async function getListApi(params?: UserTableParams) {
  return useGet('/user/list', params)
}

export async function upsertApi(params: UserTableModel) {
  return usePost('/user/upsert', params)
}

export async function updateTableColumnApi(params: UpdateTableColumn) {
  return useGet('/user/update-table-column', params)
}

export async function getUsersExcludingCurrentApi(id: string) {
  return useGet('/user/excluding-current', {'id': id})
}


export type {
  UserTableModel,
  UserTableColumn,
  UserTableParams,
  UpdateTableColumn,
}
