export const FIELDS = [
  "数と式",
  "方程式",
  "方程式の利用",
  "規則性",
  "関数",
  "図形",
  "図形の証明",
  "データの活用",
] as const;

export type MathField = (typeof FIELDS)[number];

export type ArchiveItem = {
  id: string;
  grade: 1 | 2 | 3;
  year: number;
  prefecture: string;
  field: MathField;
  unit: string;
  shortUnit: string;
  tags: string[];
  pageCount: number;
  previewPages: string[];
  contentVersion: string;
  pdfUrl: string;
  pdfFileName: string;
  fileSize: number;
};

export type ArchiveData = {
  generatedAt: string;
  releaseTag: string;
  totalItems: number;
  totalPages: number;
  items: ArchiveItem[];
};
