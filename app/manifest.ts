import type { MetadataRoute } from "next";

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "Mathmatica｜高校入試 数学単元別アーカイブ",
    short_name: "Mathmatica",
    description: "高校入試の数学大問を画像で比較・選定できる講師向けアーカイブ",
    start_url: "/",
    display: "standalone",
    background_color: "#08101f",
    theme_color: "#08101f",
    lang: "ja",
    icons: [{ src: "/icons/icon.svg", sizes: "any", type: "image/svg+xml", purpose: "any" }],
  };
}
