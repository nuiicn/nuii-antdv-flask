<script setup lang="ts">
import type { FormInstance } from 'ant-design-vue'
import { cloneDeep } from 'lodash'
import type { UserTableModel } from '@/api/customize/system/user.ts'
import { upsertApi } from '@/api/customize/system/user.ts'

const emit = defineEmits(['cancel', 'submit'])
const isUpdate = ref(false)
const visible = ref(false)

const labelCol = { style: { width: '100px' }}
const wrapperCol = { span: 24 }
const title = computed(() => {
  return isUpdate.value ? '编辑' : '新增'
})

const formRef = ref<FormInstance>()
const formData = ref<UserTableModel>({
  id: '',
  parent_id: '',
  department_id: '',
  nickname: '',
  username: '',
  email: '',
  avatar: '',
})

function open(record?: UserTableModel) {
  visible.value = true
  isUpdate.value = !!record?.id
  formData.value = cloneDeep(record) ?? {
    id: '',
    parent_id: '',
    department_id: '',
    nickname: '',
    username: '',
    email: '',
    avatar: '',
  }
}

async function handleSubmit() {
  try {
    await formRef.value?.validate()
    const { code } = await upsertApi({
      ...formData.value,
    })
    if (code === 200) {
      emit('submit')
      visible.value = false
    }
  }
  catch (errorInfo) {
    console.log('Form Validate Failed:', errorInfo)
  }
}

function handleCancel() {
  formRef.value?.resetFields()
  emit('cancel')
}

defineExpose({
  open,
})
</script>
<template>
  <a-modal v-model:open="visible" :title="title" @ok="handleSubmit" @cancel="handleCancel">
    <a-form ref="formRef" :model="formData" class="w-full" :label-col="labelCol" :wrapper-col="wrapperCol" style="margin-top: 20px">
      <a-form-item name="avatar" label="头像">
        <a-input v-model:value="formData.avatar" :maxlength="50" placeholder="" />
      </a-form-item>
      <a-form-item name="parent_id" label="直属领导">
        <a-input v-model:value="formData.parent_id" :maxlength="50" placeholder="" />
      </a-form-item>
      <a-form-item name="department_id" label="所属部门">
        <a-input v-model:value="formData.department_id" :maxlength="50" placeholder="" />
      </a-form-item>
      <a-form-item name="nickname" label="昵称" :rules="[{ required: true, message: '请输入昵称' }]">
        <a-input v-model:value="formData.nickname" :maxlength="50" placeholder="请输入昵称" />
      </a-form-item>
      <a-form-item name="username" label="用户名" :rules="[{ required: true, message: '请输入用户名' }]">
        <a-input v-model:value="formData.username" :maxlength="50" placeholder="请输入用户名" />
      </a-form-item>
      <a-form-item name="email" label="电子邮箱" :rules="[{ required: true, message: '请输入电子邮箱' }]">
        <a-input v-model:value="formData.email" :maxlength="50" placeholder="请输入电子邮箱" />
      </a-form-item>
      <a-form-item name="remark" label="备注">
        <a-textarea v-model:value="formData.remark" show-count :maxlength="200" placeholder="请输入备注" />
      </a-form-item>
    </a-form>
  </a-modal>
</template>
