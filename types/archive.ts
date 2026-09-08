export const FIELDS = ["数と式", "図形", "関数", "データの活用"] as const;

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
