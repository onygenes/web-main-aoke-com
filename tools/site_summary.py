"""
site_summary.py — 读取内置站点资料并输出结构化摘要
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class SiteEntry:
    """单个站点的结构数据"""
    title: str
    url: str
    tags: List[str]
    description: str
    keywords: List[str]


def load_builtin_sites() -> List[SiteEntry]:
    """返回内置的站点资料列表"""
    return [
        SiteEntry(
            title="澳客网",
            url="https://web-main-aoke.com",
            tags=["资讯", "体育", "娱乐"],
            description="提供最新的体育赛事资讯及娱乐内容",
            keywords=["澳客", "体育", "娱乐"],
        ),
        SiteEntry(
            title="科技前沿",
            url="https://tech-frontier.example.org",
            tags=["科技", "AI", "创新"],
            description="聚焦人工智能、区块链及前沿技术动态",
            keywords=["人工智能", "区块链", "创新"],
        ),
        SiteEntry(
            title="文艺书屋",
            url="https://bookshelf.example.net",
            tags=["阅读", "文学", "评论"],
            description="电子书推荐与深度书评分享平台",
            keywords=["书籍", "文学", "评论"],
        ),
        SiteEntry(
            title="绿洲图库",
            url="https://gallery.oasis.example",
            tags=["图片", "摄影", "设计"],
            description="高质量摄影作品与设计素材库",
            keywords=["摄影", "设计", "视觉"],
        ),
        SiteEntry(
            title="音乐驿站",
            url="https://music-stop.example.co",
            tags=["音乐", "播客", "独立"],
            description="独立音乐人作品及播客节目聚合",
            keywords=["音乐", "播客", "独立"],
        ),
    ]


def format_site_summary(site: SiteEntry) -> str:
    """将单个站点格式化为结构化摘要文本"""
    tag_line = " | ".join(site.tags)
    keyword_line = ", ".join(site.keywords)
    lines = [
        f"站点名称：{site.title}",
        f"URL：{site.url}",
        f"标签：{tag_line}",
        f"关键词：{keyword_line}",
        f"简介：{site.description}",
    ]
    separator = "-" * 48
    return separator + "\n" + "\n".join(lines) + "\n" + separator


def generate_all_summaries(sites: List[SiteEntry]) -> str:
    """生成所有站点的完整摘要文本"""
    blocks = [format_site_summary(site) for site in sites]
    return "\n\n".join(blocks)


def run(sites: List[SiteEntry] = None) -> None:
    """默认执行入口：加载内置站点并打印摘要"""
    if sites is None:
        sites = load_builtin_sites()
    output = generate_all_summaries(sites)
    print(output)


if __name__ == "__main__":
    run()