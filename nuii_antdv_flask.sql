-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Generation Time: Sep 03, 2024 at 01:07 AM
-- Server version: 5.7.44
-- PHP Version: 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nuii_antdv_flask`
--

-- --------------------------------------------------------

--
-- Table structure for table `actions`
--

CREATE TABLE `actions` (
  `id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `describe` varchar(255) DEFAULT NULL,
  `defaultCheck` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `updated_time` datetime DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `actions`
--

INSERT INTO `actions` (`id`, `name`, `describe`, `defaultCheck`, `status`, `updated_by`, `updated_time`, `created_by`, `created_time`) VALUES
(1, 'add', '新增', 0, 1, NULL, '2024-07-18 11:16:35', NULL, '2024-07-18 11:16:35'),
(2, 'query', '查询', 0, 1, NULL, '2024-07-18 11:17:36', NULL, '2024-07-18 11:17:36'),
(3, 'get', '详情', 0, 1, NULL, '2024-07-18 11:17:36', NULL, '2024-07-18 11:17:36'),
(4, 'update', '修改', 0, 1, NULL, '2024-07-18 13:17:51', NULL, '2024-07-18 13:17:51'),
(5, 'delete', '删除', 0, 1, NULL, '2024-07-18 13:17:51', NULL, '2024-07-18 13:17:51'),
(6, 'import', '导入', 0, 1, NULL, '2024-07-18 13:19:27', NULL, '2024-07-18 13:19:27'),
(7, 'export', '导出', 0, 1, NULL, '2024-07-18 13:19:27', NULL, '2024-07-18 13:19:27');

-- --------------------------------------------------------

--
-- Table structure for table `chats`
--

CREATE TABLE `chats` (
  `id` int(11) NOT NULL,
  `owner_id` int(11) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `updated_time` datetime DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `chat_messages`
--

CREATE TABLE `chat_messages` (
  `id` int(11) NOT NULL,
  `owner_id` int(11) DEFAULT NULL,
  `chat_id` int(11) DEFAULT NULL,
  `message` text,
  `status` int(11) DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `updated_time` datetime DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `departments`
--

CREATE TABLE `departments` (
  `id` int(11) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `description` text,
  `status` int(11) DEFAULT NULL,
  `updated_by` int(11) NOT NULL,
  `updated_time` datetime DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `departments`
--

INSERT INTO `departments` (`id`, `parent_id`, `name`, `description`, `status`, `updated_by`, `updated_time`, `created_by`, `created_time`) VALUES
(1, 0, '全球总部', 'Global Headquarters', 1, 1, '2024-09-03 06:34:31', 1, '2024-09-03 06:34:31'),
(2, 1, '亚太区', 'Asia-Pacific Region, APAC', 1, 1, '2024-09-02 22:12:37', 1, '2024-09-02 22:12:37'),
(3, 2, '中国区', 'China Region', 1, 1, '2024-09-03 07:15:13', 1, '2024-09-03 07:15:13'),
(4, 3, '华北区', 'North China Region', 1, 1, '2024-09-03 07:15:13', 1, '2024-09-03 07:15:13');

-- --------------------------------------------------------

--
-- Table structure for table `llms`
--

CREATE TABLE `llms` (
  `id` int(11) NOT NULL,
  `owner_id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `description` text,
  `icon` varchar(100) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `updated_time` datetime DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `llm_api_keys`
--

CREATE TABLE `llm_api_keys` (
  `id` int(11) NOT NULL,
  `owner_id` int(11) NOT NULL,
  `llm_id` int(11) DEFAULT NULL,
  `key` varchar(50) DEFAULT NULL,
  `url` varchar(50) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `updated_time` datetime DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `llm_prompts`
--

CREATE TABLE `llm_prompts` (
  `id` int(11) NOT NULL,
  `owner_id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `content` text,
  `status` int(11) DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `updated_time` datetime DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `permissions`
--

CREATE TABLE `permissions` (
  `id` int(11) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `code` varchar(50) DEFAULT NULL,
  `url` varchar(100) DEFAULT NULL,
  `icon` varchar(100) DEFAULT NULL,
  `actions` text,
  `level` int(11) DEFAULT NULL,
  `sort` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `updated_time` datetime DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `permissions`
--

INSERT INTO `permissions` (`id`, `parent_id`, `name`, `code`, `url`, `icon`, `actions`, `level`, `sort`, `status`, `updated_by`, `updated_time`, `created_by`, `created_time`) VALUES
(1, NULL, '仪表盘', 'dashboard', NULL, NULL, '[{\"action\":\"add\",\"defaultCheck\":false,\"describe\":\"新增\"},{\"action\":\"query\",\"defaultCheck\":false,\"describe\":\"查询\"},{\"action\":\"get\",\"defaultCheck\":false,\"describe\":\"详情\"},{\"action\":\"update\",\"defaultCheck\":false,\"describe\":\"修改\"},{\"action\":\"delete\",\"defaultCheck\":false,\"describe\":\"删除\"}]', NULL, NULL, 1, NULL, '2024-07-16 16:25:04', NULL, '2024-07-16 16:25:04'),
(2, NULL, '异常页面权限', 'exception', NULL, NULL, '[{\"action\":\"add\",\"defaultCheck\":false,\"describe\":\"新增\"},{\"action\":\"query\",\"defaultCheck\":false,\"describe\":\"查询\"},{\"action\":\"get\",\"defaultCheck\":false,\"describe\":\"详情\"},{\"action\":\"update\",\"defaultCheck\":false,\"describe\":\"修改\"},{\"action\":\"delete\",\"defaultCheck\":false,\"describe\":\"删除\"}]', NULL, NULL, 1, NULL, '2024-07-16 16:26:43', NULL, '2024-07-16 16:26:43'),
(3, NULL, '结果权限', 'result', NULL, NULL, '[{\"action\":\"add\",\"defaultCheck\":false,\"describe\":\"新增\"},{\"action\":\"query\",\"defaultCheck\":false,\"describe\":\"查询\"},{\"action\":\"get\",\"defaultCheck\":false,\"describe\":\"详情\"},{\"action\":\"update\",\"defaultCheck\":false,\"describe\":\"修改\"},{\"action\":\"delete\",\"defaultCheck\":false,\"describe\":\"删除\"}]', NULL, NULL, 1, NULL, '2024-07-16 16:27:29', NULL, '2024-07-16 16:27:29'),
(4, NULL, '详细页权限', 'profile', NULL, NULL, '[{\"action\":\"add\",\"defaultCheck\":false,\"describe\":\"新增\"},{\"action\":\"query\",\"defaultCheck\":false,\"describe\":\"查询\"},{\"action\":\"get\",\"defaultCheck\":false,\"describe\":\"详情\"},{\"action\":\"update\",\"defaultCheck\":false,\"describe\":\"修改\"},{\"action\":\"delete\",\"defaultCheck\":false,\"describe\":\"删除\"}]', NULL, NULL, 1, NULL, '2024-07-16 16:27:58', NULL, '2024-07-16 16:27:58'),
(5, NULL, '表格权限', 'table', NULL, NULL, '[{\"action\":\"add\",\"defaultCheck\":false,\"describe\":\"新增\"},{\"action\":\"import\",\"defaultCheck\":false,\"describe\":\"导入\"},{\"action\":\"get\",\"defaultCheck\":false,\"describe\":\"详情\"},{\"action\":\"update\",\"defaultCheck\":false,\"describe\":\"修改\"}]', NULL, NULL, 1, NULL, '2024-07-16 16:28:24', NULL, '2024-07-16 16:28:24'),
(6, NULL, '表单权限', 'form', NULL, NULL, '[{\"action\":\"add\",\"defaultCheck\":false,\"describe\":\"新增\"},{\"action\":\"get\",\"defaultCheck\":false,\"describe\":\"详情\"},{\"action\":\"query\",\"defaultCheck\":false,\"describe\":\"查询\"},{\"action\":\"update\",\"defaultCheck\":false,\"describe\":\"修改\"},{\"action\":\"delete\",\"defaultCheck\":false,\"describe\":\"删除\"}]', NULL, NULL, 1, NULL, '2024-07-16 16:28:49', NULL, '2024-07-16 16:28:49'),
(7, NULL, '订单管理', 'order', NULL, NULL, '[{\"action\":\"add\",\"defaultCheck\":false,\"describe\":\"新增\"},{\"action\":\"query\",\"defaultCheck\":false,\"describe\":\"查询\"},{\"action\":\"get\",\"defaultCheck\":false,\"describe\":\"详情\"},{\"action\":\"update\",\"defaultCheck\":false,\"describe\":\"修改\"},{\"action\":\"delete\",\"defaultCheck\":false,\"describe\":\"删除\"}]', NULL, NULL, 1, NULL, '2024-07-16 16:29:09', NULL, '2024-07-16 16:29:09'),
(8, NULL, '权限管理', 'permission', NULL, NULL, '[{\"action\":\"add\",\"defaultCheck\":false,\"describe\":\"新增\"},{\"action\":\"get\",\"defaultCheck\":false,\"describe\":\"详情\"},{\"action\":\"update\",\"defaultCheck\":false,\"describe\":\"修改\"},{\"action\":\"delete\",\"defaultCheck\":false,\"describe\":\"删除\"}]', NULL, NULL, 1, NULL, '2024-07-16 16:29:32', NULL, '2024-07-16 16:29:32'),
(9, NULL, '角色管理', 'role', NULL, NULL, '[{\"action\":\"add\",\"defaultCheck\":false,\"describe\":\"新增\"},{\"action\":\"get\",\"defaultCheck\":false,\"describe\":\"详情\"},{\"action\":\"update\",\"defaultCheck\":false,\"describe\":\"修改\"},{\"action\":\"delete\",\"defaultCheck\":false,\"describe\":\"删除\"}]', NULL, NULL, 1, NULL, '2024-07-16 16:29:47', NULL, '2024-07-16 16:29:47'),
(10, NULL, '桌子管理', 'table', NULL, NULL, '[{\"action\":\"add\",\"defaultCheck\":false,\"describe\":\"新增\"},{\"action\":\"get\",\"defaultCheck\":false,\"describe\":\"详情\"},{\"action\":\"query\",\"defaultCheck\":false,\"describe\":\"查询\"},{\"action\":\"update\",\"defaultCheck\":false,\"describe\":\"修改\"},{\"action\":\"delete\",\"defaultCheck\":false,\"describe\":\"删除\"}]', NULL, NULL, 1, NULL, '2024-07-16 16:30:08', NULL, '2024-07-16 16:30:08'),
(11, NULL, '用户管理', 'user', NULL, NULL, '[{\"action\":\"add\",\"defaultCheck\":false,\"describe\":\"新增\"},{\"action\":\"import\",\"defaultCheck\":false,\"describe\":\"导入\"},{\"action\":\"get\",\"defaultCheck\":false,\"describe\":\"详情\"},{\"action\":\"update\",\"defaultCheck\":false,\"describe\":\"修改\"},{\"action\":\"delete\",\"defaultCheck\":false,\"describe\":\"删除\"},{\"action\":\"export\",\"defaultCheck\":false,\"describe\":\"导出\"}]\r\n', NULL, NULL, 1, NULL, '2024-07-16 16:30:25', NULL, '2024-07-16 16:30:25');

-- --------------------------------------------------------

--
-- Table structure for table `permission_actions`
--

CREATE TABLE `permission_actions` (
  `id` int(11) NOT NULL,
  `permission_id` int(11) DEFAULT NULL,
  `action_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `permission_actions`
--

INSERT INTO `permission_actions` (`id`, `permission_id`, `action_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4),
(5, 1, 5),
(6, 2, 1),
(7, 2, 2),
(8, 2, 3),
(9, 2, 4),
(10, 2, 5),
(11, 3, 1),
(12, 3, 2),
(13, 3, 3),
(14, 3, 4),
(15, 3, 5),
(16, 4, 1),
(17, 4, 2),
(18, 4, 3),
(19, 4, 4),
(20, 4, 5),
(21, 5, 1),
(22, 5, 6),
(23, 5, 3),
(24, 5, 4),
(25, 6, 1),
(26, 6, 2),
(27, 6, 3),
(28, 6, 4),
(29, 6, 5),
(30, 7, 1),
(31, 7, 2),
(32, 7, 3),
(33, 7, 4),
(34, 7, 5),
(35, 8, 1),
(36, 8, 3),
(37, 8, 4),
(38, 8, 5),
(39, 9, 1),
(40, 9, 3),
(41, 9, 4),
(42, 9, 5),
(43, 10, 1),
(44, 10, 3),
(45, 10, 3),
(46, 10, 4),
(47, 10, 5),
(48, 11, 1),
(49, 11, 3),
(50, 11, 4),
(51, 11, 5),
(52, 11, 6),
(53, 11, 7);

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `description` text,
  `code` varchar(50) DEFAULT NULL,
  `describe` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `updated_time` datetime DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`id`, `name`, `description`, `code`, `describe`, `status`, `updated_by`, `updated_time`, `created_by`, `created_time`) VALUES
(1, '管理员', NULL, 'admin', '拥有所有权限', 1, 1, '2024-07-16 16:19:16', 1, '2024-07-16 16:19:16'),
(2, '会员', NULL, 'member', '普通会员', 1, 1, '2024-07-16 23:57:36', 1, '2024-07-16 23:57:36');

-- --------------------------------------------------------

--
-- Table structure for table `role_permissions`
--

CREATE TABLE `role_permissions` (
  `id` int(11) NOT NULL,
  `permission_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `role_permissions`
--

INSERT INTO `role_permissions` (`id`, `permission_id`, `role_id`) VALUES
(1, 1, 1),
(2, 4, 1),
(3, 8, 1),
(4, 9, 1),
(5, 11, 1),
(6, 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `sys_logs`
--

CREATE TABLE `sys_logs` (
  `id` int(11) NOT NULL,
  `type` int(11) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `data` text,
  `status` int(11) DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `updated_time` datetime DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  `nickname` varchar(50) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `login_time` datetime DEFAULT NULL,
  `login_status` int(11) DEFAULT NULL,
  `avatar` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `updated_time` datetime DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `parent_id`, `department_id`, `nickname`, `username`, `email`, `password`, `login_time`, `login_status`, `avatar`, `status`, `updated_by`, `updated_time`, `created_by`, `created_time`) VALUES
(1, 0, 0, 'nuii', 'nuii', 'nuii-@gmail.com', 'scrypt:32768:8:1$pwxyEFYp8ZjTyGfD$65b731398611cbb8ef6e83d4499f6b499aeed88a9ff7bafd3dbac9f89e15f1c6a38d8f435de102e2179fe8d8b79056595889d78f00ac1fc2f982443592722275', '2024-08-25 19:12:36', 0, NULL, 0, 1, '2024-07-24 23:52:41', 1, '2024-07-14 13:23:27'),
(2, 0, 0, 'nuii2', 'nuii2', 'nuii2@gmail.com', 'scrypt:32768:8:1$pwxyEFYp8ZjTyGfD$65b731398611cbb8ef6e83d4499f6b499aeed88a9ff7bafd3dbac9f89e15f1c6a38d8f435de102e2179fe8d8b79056595889d78f00ac1fc2f982443592722275', '2024-08-25 19:12:36', 0, NULL, 1, 1, '2024-07-17 09:39:03', 1, '2024-07-16 19:29:25'),
(5, 0, 0, 'siping 6', 'siping 6', 'sipings06@gmail.com', 'pbkdf2:sha256:600000$mjq5XHYH9D9bCAJZ$0f1ca6b4a346a5854d7868e6b94e728e2fa63bc5271b130b02bd95c59e648b55', '2024-08-25 19:12:36', 0, NULL, 1, 0, '2024-08-28 23:25:02', 0, '2024-08-25 19:12:36'),
(6, 1, 0, 'siping', 'siping', 'siping', 'pbkdf2:sha256:600000$pGhlUix3lB6gamJI$9d6ff70d90a65a0a8d0289622ad206382067821528c24632f6e0e9df161b4604', '2024-09-02 16:39:51', 0, NULL, 1, 0, '2024-09-02 16:40:40', 0, '2024-09-02 16:39:51');

-- --------------------------------------------------------

--
-- Table structure for table `user_roles`
--

CREATE TABLE `user_roles` (
  `id` int(11) NOT NULL,
  `role_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_roles`
--

INSERT INTO `user_roles` (`id`, `role_id`, `user_id`) VALUES
(1, 1, 1),
(2, 2, 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `actions`
--
ALTER TABLE `actions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `chats`
--
ALTER TABLE `chats`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `chat_messages`
--
ALTER TABLE `chat_messages`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `departments`
--
ALTER TABLE `departments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `llms`
--
ALTER TABLE `llms`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `llm_api_keys`
--
ALTER TABLE `llm_api_keys`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `llm_prompts`
--
ALTER TABLE `llm_prompts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `permissions`
--
ALTER TABLE `permissions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `permission_actions`
--
ALTER TABLE `permission_actions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `role_permissions`
--
ALTER TABLE `role_permissions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `permission_id` (`permission_id`),
  ADD KEY `role_id` (`role_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `login_name` (`username`),
  ADD UNIQUE KEY `login_email` (`email`);

--
-- Indexes for table `user_roles`
--
ALTER TABLE `user_roles`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `role_id` (`role_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `actions`
--
ALTER TABLE `actions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `chats`
--
ALTER TABLE `chats`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `chat_messages`
--
ALTER TABLE `chat_messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `departments`
--
ALTER TABLE `departments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `llms`
--
ALTER TABLE `llms`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `llm_api_keys`
--
ALTER TABLE `llm_api_keys`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `llm_prompts`
--
ALTER TABLE `llm_prompts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `permissions`
--
ALTER TABLE `permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `permission_actions`
--
ALTER TABLE `permission_actions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `role_permissions`
--
ALTER TABLE `role_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `user_roles`
--
ALTER TABLE `user_roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `role_permissions`
--
ALTER TABLE `role_permissions`
  ADD CONSTRAINT `role_permissions_ibfk_1` FOREIGN KEY (`permission_id`) REFERENCES `permissions` (`id`),
  ADD CONSTRAINT `role_permissions_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`);

--
-- Constraints for table `user_roles`
--
ALTER TABLE `user_roles`
  ADD CONSTRAINT `user_roles_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `user_roles_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
