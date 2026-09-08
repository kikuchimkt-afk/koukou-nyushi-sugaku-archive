import type { Metadata, Viewport } from "next";
import "./globals.css";

export const metadata: Metadata = {
  metadataBase: new URL("https://koukou-nyushi-sugaku-archive.vercel.app"),
  title: "Mathmatica｜高校入試 数学単元別アーカイブ",
  description: "高校入試の数学大問を、学年・領域・年度・県・単元から探して画像で比較できる講師向けアーカイブ。",
  applicationName: "Mathmatica",
  openGraph: {
    title: "Mathmatica｜高校入試 数学単元別アーカイブ",
    description: "問題を画像で見比べ、授業に合う大問を素早く選定。",
    type: "website",
    locale: "ja_JP",
    images: [{ url: "/images/hero-math.svg", width: 1920, height: 1080 }],
  },
  icons: [{ url: "/icons/icon.svg", type: "image/svg+xml" }],
};

export const viewport: Viewport = {
  themeColor: "#08101f",
  colorScheme: "dark",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="ja">
      <body>{children}</body>
    </html>
  );
}
