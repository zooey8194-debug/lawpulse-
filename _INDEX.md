---
title: LawPulse 索引仪表盘
tags: [系统/索引]
---

# LawPulse 索引仪表盘

> 律脉LawPulse — 律师全生命周期智能成长系统
> 最后更新: <% tp.date.now("YYYY-MM-DD HH:mm") %>

---

## 一、活跃案件

```dataview
TABLE case_type AS 案由, court AS 法院, status AS 状态, plaintiff AS 原告, defendant AS 被告
FROM "01-案件 (Cases)"
WHERE status = "代理中"
SORT created DESC
```

---

## 二、高风险当事人预警

```dataview
TABLE role AS 角色, risk_level AS 风险等级, emotion_baseline AS 情绪底色, connection AS 关联案件
FROM "02-人物 (Entities)"
WHERE role = "当事人" AND risk_level = "高"
SORT created DESC
```

---

## 三、待复盘案件

```dataview
TABLE case_connection AS 关联案件, review_type AS 复盘类型, outcome AS 结果, rating AS 评分
FROM "04-复盘 (Reviews)"
WHERE review_type = "结案复盘"
SORT created DESC
LIMIT 10
```

---

## 四、法官画像速览

```dataview
TABLE position AS 职位, connection AS 关联案件, data_source AS 数据来源
FROM "02-人物 (Entities)"
WHERE contains(role, "法官")
SORT created DESC
```

---

## 五、对方律师追踪

```dataview
TABLE law_firm AS 律所, domain AS 擅长领域, years_experience AS 从业年限
FROM "02-人物 (Entities)"
WHERE contains(role, "对方律师")
SORT created DESC
```

---

## 六、最近更新

```dataview
TABLE file.mtime AS 更新时间, status AS 状态
FROM "01-案件 (Cases)"
SORT file.mtime DESC
LIMIT 5
```

